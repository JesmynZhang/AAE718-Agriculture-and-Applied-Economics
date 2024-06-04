import pandas as pd
import os
import matplotlib.pyplot as plt

# Problem 1: Function to list all CSV files in a directory
def csv_files(directory):
    csv_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".csv"):
                csv_list.append(os.path.join(root, file))
    print(f"Found {len(csv_list)} CSV files in directory: {directory}")
    return csv_list

# Problem 2: Function to load a CSV file and add a year column
def load_emission_csv(file_path, year):
    df = pd.read_csv(file_path)
    df['year'] = year
    return df

# Problem 3: Function to load all emissions data from a directory
def load_emissions(directory):
    csv_list = csv_files(directory)
    data_frames = [load_emission_csv(file, os.path.basename(file).split('.')[0]) for file in csv_list]
    combined_df = pd.concat(data_frames, ignore_index=True)
    return combined_df

# Problem 4: Function to merge emissions data with country codes
def merge_emissions_with_country_codes(emissions_directory, country_code_path):
    # Load the emissions data
    emissions_df = load_emissions(emissions_directory)
    
    # Load the country codes data
    country_codes_df = pd.read_csv(country_code_path)
    
    # Display column names for debugging
    print("Emissions DataFrame columns:", emissions_df.columns)
    print("Country Codes DataFrame columns:", country_codes_df.columns)
    
    # Rename 'name' column to 'Country' in country codes data frame
    country_codes_df.rename(columns={'name': 'Country'}, inplace=True)
    
    # Merge the data frames on the Country column
    merged_df = pd.merge(emissions_df, country_codes_df, how='left', on='Country')
    
    # Display merged DataFrame columns for debugging
    print("Merged DataFrame columns:", merged_df.columns)
    
    return merged_df

# Example usage for Problem 4
emissions_directory = '.'
country_code_path = 'country_codes.csv'
merged_df = merge_emissions_with_country_codes(emissions_directory, country_code_path)
print(merged_df.head())

# Problem 5: Create and display graphs

# Graph 1: Total CO2 Emissions by Region
def plot_total_co2_by_region(df):
    # Display columns for debugging
    print("Columns available for plotting:", df.columns)
    
    # Group by 'region_y' and sum 'Emissions.Type.CO2'
    region_co2 = df.groupby('region_y')['Emissions.Type.CO2'].sum()
    plt.figure(figsize=(10, 6))
    region_co2.plot(kind='bar')
    plt.title('Total CO2 Emissions by Region')
    plt.xlabel('Region')
    plt.ylabel('Total CO2 Emissions')
    plt.savefig('total_co2_by_region.png')
    plt.show()
    plt.close()  # Close the plot automatically

# Graph 2: Total CO2 Emissions by Year
def plot_total_co2_by_year(df):
    # Group by 'year' and sum 'Emissions.Type.CO2'
    year_co2 = df.groupby('year')['Emissions.Type.CO2'].sum()
    plt.figure(figsize=(10, 6))
    year_co2.plot(kind='line')
    plt.title('Total CO2 Emissions by Year')
    plt.xlabel('Year')
    plt.ylabel('Total CO2 Emissions')
    plt.savefig('total_co2_by_year.png')
    plt.show()
    plt.close()  # Close the plot automatically

# Graph 3: CO2 Emissions Distribution by Region in 1990
def plot_co2_distribution_by_region(df, year='1990'):
    year_data = df[df['year'] == year]
    plt.figure(figsize=(10, 6))
    year_data.boxplot(column='Emissions.Type.CO2', by='region_y', grid=False)
    plt.title('CO2 Emissions Distribution by Region in 1990')
    plt.xlabel('Region')
    plt.ylabel('CO2 Emissions')
    plt.suptitle('')  # Suppress the default title
    plt.savefig(f'co2_distribution_by_region_{year}.png')
    plt.show()
    plt.close()  # Close the plot automatically

# Example usage for Problem 5
plot_total_co2_by_region(merged_df)
plot_total_co2_by_year(merged_df)
plot_co2_distribution_by_region(merged_df, year='1990')

# Problem 6: Function to clean dirty data
def clean_dirty_data(file_path):
    # Load the data
    dirty_data = pd.read_csv(file_path)

    # Extract column names for segments and ship modes from the first row
    segments = ["Consumer", "Corporate", "Home Office"]
    ship_modes = dirty_data.iloc[0, 1:5].tolist()

    # Initialize an empty list to store the cleaned data
    clean_data = []

    # Iterate through the data rows
    for idx, row in dirty_data.iterrows():
        if idx > 1:
            for i, segment in enumerate(segments):
                if not pd.isna(row[2*i + 2]):
                    clean_data.append({
                        'order id': row[0],
                        'segment': segment,
                        'ship mode': ship_modes[i],
                        'sales': row[2*i + 2]
                    })
    
    # Create a DataFrame from the cleaned data
    clean_df = pd.DataFrame(clean_data)
    
    return clean_df

# Example usage for Problem 6
file_path_dirty = 'dirty_data_01.csv'
cleaned_df = clean_dirty_data(file_path_dirty)
print(cleaned_df.head())

# Problem 7: Function to load and process school data
import pandas as pd

def parse_school_data(data_path, layout_path):
    # Define the fixed widths based on the provided layout information
    column_widths = [2, 1, 5, 1, 72, 1, 8, 1, 8, 1, 8, 1, 21]
    column_names = [
        'FIPS State Code', 'Unused1', 'District ID', 'Unused2', 'District Name', 'Unused3', 
        'Total Population', 'Unused4', 'School-age Population', 'Unused5', 
        'School-age Poverty Population', 'Unused6', 'File Info'
    ]
    
    # Load the data file
    df = pd.read_fwf(data_path, widths=column_widths, header=None, encoding='latin-1', names=column_names)
    
    # Drop the unnecessary columns
    df.drop(columns=['Unused1', 'Unused2', 'Unused3', 'Unused4', 'Unused5', 'Unused6', 'File Info'], inplace=True)
    
    return df

# Paths to the provided files
data_path = 'school_data/ussd20.txt'
layout_path = 'school_data/2020-district-layout.txt'

# Load and process the school data
school_df = parse_school_data(data_path, layout_path)

# Display the first few rows of the processed dataframe
print(school_df.head())

