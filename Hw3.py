import pandas as pd
import matplotlib.pyplot as plt
import zipfile

# Problem 01: Load data function
def load_data(file_path):
    df = pd.read_csv(file_path)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    return df

# Problem 02: Methane aggregation function
def methane_aggregation(file_path):
    df = load_data(file_path)
    
    subset = df[(df['region'] != 'World') & (df['type'] == 'Agriculture')]
    subset_emissions_sum = subset['emissions'].sum()
    
    world_agriculture_emissions_sum = df[(df['region'] == 'World') & (df['type'] == 'Agriculture')]['emissions'].sum()
    
    return subset_emissions_sum - world_agriculture_emissions_sum

# Problem 03: Unique segments function
def problem_03(file_path):
    df = load_data(file_path)
    
    subset = df[(df['region'] != 'World') & (df['type'] == 'Agriculture')]
    unique_segments = subset['segment'].unique()
    
    return unique_segments

# Problem 04: Region mean function
def region_mean(file_path):
    df = load_data(file_path)
    region_averages = df.groupby('region')['emissions'].mean().reset_index()
    
    return region_averages

# Problem 05: Region total mean function
def region_total_mean(file_path):
    df = load_data(file_path)
    df_filtered = df[df['segment'] == 'Total']
    region_averages = df_filtered.groupby('region')['emissions'].mean().reset_index()
    
    return region_averages

# Problem 06: Methane graphs function
def methane_graphs(file_path):
    df = load_data(file_path)

    # Boxplot 1: Aggregated by region
    plt.figure(figsize=(15, 10))
    df.boxplot(column='emissions', by='region', vert=False)
    plt.title('Aggregated by region')
    plt.suptitle('')
    plt.xlabel('Emissions')
    plt.ylabel('Region')
    plt.tight_layout()
    plt.savefig('boxplot_region.png')
    plt.close()

    # Boxplot 2: Aggregated by region, excluding World
    plt.figure(figsize=(15, 10))
    df_excluding_world = df[df['region'] != 'World']
    df_excluding_world.boxplot(column='emissions', by='region', vert=False)
    plt.title('Aggregated by region, excluding World')
    plt.suptitle('')
    plt.xlabel('Emissions')
    plt.ylabel('Region')
    plt.tight_layout()
    plt.savefig('boxplot_region_excluding_world.png')
    plt.close()

    # Boxplot 3: Aggregated by region, excluding World and only including Total
    plt.figure(figsize=(15, 10))
    df_excluding_world_total = df_excluding_world[df_excluding_world['segment'] == 'Total']
    df_excluding_world_total.boxplot(column='emissions', by='region', vert=False)
    plt.title('Aggregated by region, excluding World and only including Total')
    plt.suptitle('')
    plt.xlabel('Emissions')
    plt.ylabel('Region')
    plt.tight_layout()
    plt.savefig('boxplot_region_excluding_world_total.png')
    plt.close()

    # Boxplot 4: Aggregated by segment, excluding World and Total
    plt.figure(figsize=(15, 10))
    df_excluding_world_segment = df_excluding_world[df_excluding_world['segment'] != 'Total']
    df_excluding_world_segment.boxplot(column='emissions', by='segment', vert=False)
    plt.title('Aggregated by segment, excluding World and Total')
    plt.suptitle('')
    plt.xlabel('Emissions')
    plt.ylabel('Segment')
    plt.tight_layout()
    plt.savefig('boxplot_segment_excluding_world_total.png')
    plt.close()

    # Boxplot 5: One interesting plot - Example: Emissions by type
    plt.figure(figsize=(15, 10))
    df.boxplot(column='emissions', by='type', vert=False)
    plt.title('Aggregated by type')
    plt.suptitle('')
    plt.xlabel('Emissions')
    plt.ylabel('Type')
    plt.tight_layout()
    plt.savefig('boxplot_type.png')
    plt.close()

if __name__ == "__main__":
    file_path = "Methane_final.csv"
    
    result = methane_aggregation(file_path)
    print("Result of methane_aggregation:", result)
    
    unique_segments = problem_03(file_path)
    print("Unique segments in the subset:", unique_segments)
    
    region_averages = region_mean(file_path)
    print("Region Averages DataFrame:")
    print(region_averages)
    
    region_total_averages = region_total_mean(file_path)
    print("Region Total Averages DataFrame:")
    print(region_total_averages)

    methane_graphs(file_path)

# Problem_07: Function to load the Animal Crossing accessories dataset from a zip file
def animal_crossing(zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        file_list = zip_ref.namelist()
       
        accessories_file = [file for file in file_list if 'accessories.csv' in file][0]
        
        with zip_ref.open(accessories_file) as file:
            df = pd.read_csv(file)
    return df

# Problem_08: Function to find the item with the largest sell price
def sell_price(zip_file_path):
    
    df = animal_crossing(zip_file_path)
    
    df['Sell'] = pd.to_numeric(df['Sell'], errors='coerce')
    df.dropna(subset=['Sell'], inplace=True)
    
    max_sell_price_item = df.loc[df['Sell'].idxmax()]['Name']
    return max_sell_price_item

# Problem_09: Function to find the item with the smallest difference between buy and sell price
def smallest_diff(zip_file_path):
   
    df = animal_crossing(zip_file_path)
    
    df['Buy'] = pd.to_numeric(df['Buy'], errors='coerce')
    df['Sell'] = pd.to_numeric(df['Sell'], errors='coerce')
    df.dropna(subset=['Buy', 'Sell'], inplace=True)
    
    df['Diff'] = df['Buy'] - df['Sell']

    min_diff_item = df.loc[df['Diff'].abs().idxmin()]['Name']
    return min_diff_item

if __name__ == "__main__":
    zip_file_path = "Animal_Crossing.zip"
    
    animal_crossing_df = animal_crossing(zip_file_path)
    print(animal_crossing_df.head())

    columns = animal_crossing_df.columns
    print("Columns in the Animal Crossing accessories dataset:")
    for column in columns:
        print(column)

    item_name = sell_price(zip_file_path)
    print("Item with the largest sell price:", item_name)
   
    smallest_diff_item = smallest_diff(zip_file_path)
    print("Item with the smallest difference between buy and sell price:", smallest_diff_item)
