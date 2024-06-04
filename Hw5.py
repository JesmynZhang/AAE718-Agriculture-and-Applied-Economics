import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


#Problem_01
height_weight = pd.read_csv('SOCR-HeightWeight.csv')

def problem_1():
    # Matplotlib
    plt.figure(figsize=(10, 6))
    plt.scatter(height_weight['Height(Inches)'], height_weight['Weight(Pounds)'])
    plt.title('Scatter Plot of Height vs Weight (Matplotlib)')
    plt.xlabel('Height (Inches)')
    plt.ylabel('Weight (Pounds)')
    plt.grid(True)
    plt.savefig('problem_1_matplotlib.png')
    plt.show()

    # Seaborn 
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=height_weight, x='Height(Inches)', y='Weight(Pounds)')
    plt.title('Scatter Plot of Height vs Weight (Seaborn)')
    plt.xlabel('Height (Inches)')
    plt.ylabel('Weight (Pounds)')
    plt.savefig('problem_1_seaborn.png')
    plt.show()

problem_1()

#Problem_02
def problem_2():
    # Matplotlib 
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    
    ax1.hist(height_weight['Height(Inches)'], bins=20, color='blue', edgecolor='black')
    ax1.set_title('Height Distribution')
    ax1.set_xlabel('Height (Inches)')
    ax1.set_ylabel('Count')
    
    ax2.hist(height_weight['Weight(Pounds)'], bins=20, color='blue', edgecolor='black')
    ax2.set_title('Weight Distribution')
    ax2.set_xlabel('Weight (Pounds)')
    ax2.set_ylabel('Count')
    
    plt.suptitle('Histograms of Height and Weight (Matplotlib)')
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig('problem_2_matplotlib.png')
    plt.show()
    
    # Seaborn
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    sns.histplot(height_weight['Height(Inches)'], bins=20, kde=False, color='blue')
    plt.title('Height Distribution')
    plt.xlabel('Height (Inches)')
    plt.ylabel('Count')
    
    plt.subplot(1, 2, 2)
    sns.histplot(height_weight['Weight(Pounds)'], bins=20, kde=False, color='blue')
    plt.title('Weight Distribution')
    plt.xlabel('Weight (Pounds)')
    plt.ylabel('Count')
    
    plt.suptitle('Histograms of Height and Weight (Seaborn)')
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig('problem_2_seaborn.png')
    plt.show()

problem_2()

#Problem_03
def problem_3():
    # Matplotlib 
    plt.figure(figsize=(10, 6))
    plt.scatter(height_weight['Height(Inches)'], height_weight['Weight(Pounds)'], color='black')
    sns.regplot(x='Height(Inches)', y='Weight(Pounds)', data=height_weight, scatter=False, color='blue')
    plt.title('Scatter Plot with Regression Line (Matplotlib)')
    plt.xlabel('Height (Inches)')
    plt.ylabel('Weight (Pounds)')
    plt.savefig('problem_3_matplotlib.png')
    plt.show()

    # Seaborn 
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=height_weight, x='Height(Inches)', y='Weight(Pounds)', color='black')
    sns.regplot(data=height_weight, x='Height(Inches)', y='Weight(Pounds)', scatter=False, color='blue')
    plt.title('Scatter Plot with Regression Line (Seaborn)')
    plt.xlabel('Height (Inches)')
    plt.ylabel('Weight (Pounds)')
    plt.savefig('problem_3_seaborn.png')
    plt.show()

problem_3()

#Problem_04

company_sales_data = pd.read_csv('company_sales_data.csv')

def problem_4_1():
    plt.figure(figsize=(10, 6))
    plt.plot(company_sales_data['month_number'], company_sales_data['total_profit'], marker='o', linestyle='-', color='b')
    plt.title('Total Profit over Months')
    plt.xlabel('Month')
    plt.ylabel('Total Profit')
    plt.grid(True)
    plt.savefig('problem_4_1.png')
    plt.show()

def problem_4_2():
    plt.figure(figsize=(12, 8))
    for product in ['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']:
        plt.plot(company_sales_data['month_number'], company_sales_data[product], marker='o', linestyle='-', label=product)
    plt.title('Sales of Each Product over Time')
    plt.xlabel('Month')
    plt.ylabel('Sales Units')
    plt.legend()
    plt.grid(True)
    plt.savefig('problem_4_2.png')
    plt.show()

def problem_4_3():
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=company_sales_data, x='facecream', y='facewash')
    plt.title('Relationship between Facecream and Facewash Sales')
    plt.xlabel('Facecream Sales')
    plt.ylabel('Facewash Sales')
    plt.grid(True)
    plt.savefig('problem_4_3.png')
    plt.show()

problem_4_1()
problem_4_2()
problem_4_3()

#Problem_05

#Selected Data
crop_production_data = pd.read_csv('crop_production.csv')
print(crop_production_data.head())
average_production_by_country = crop_production_data.groupby('LOCATION')['Value'].mean()
print(average_production_by_country)
selected_locations = average_production_by_country.sort_values(ascending=False).head(7).index.tolist()
print(selected_locations)

# filtered data for grapha 1
filtered_data = crop_production_data[crop_production_data['LOCATION'].isin(selected_locations)]

# Generated Graphs
def problem_5_1_adjusted():
    g = sns.catplot(y='SUBJECT', hue='LOCATION', data=filtered_data, kind='count', height=10, aspect=1.5, palette='viridis')
    g.set_axis_labels("Count", "Crop Type")
    g.fig.suptitle('Distribution of Crop Yield by Selected Locations', y=1.02)
    plt.savefig('problem_5_1_adjusted.png')
    plt.show()

def problem_5_2():
    plt.figure(figsize=(12, 8))
    sns.countplot(y='LOCATION', data=crop_production_data, order=crop_production_data['LOCATION'].value_counts().index)
    plt.title('Production by Country')
    plt.xlabel('Count')
    plt.ylabel('Country')
    plt.savefig('problem_5_2.png')
    plt.show()

def problem_5_3():
    plt.figure(figsize=(12, 8))
    sns.lineplot(x='TIME', y='Value', hue='SUBJECT', data=crop_production_data, errorbar=None)
    plt.title('Production over Years')
    plt.xlabel('Year')
    plt.ylabel('Production (TONNE_HA)')
    plt.legend(title='Crop Type', loc='upper right')
    plt.savefig('problem_5_3.png')
    plt.show()

problem_5_1_adjusted()
problem_5_2()
problem_5_3()

#Problem_06

crop_production_data = pd.read_csv('crop_production.csv')

def problem_5_1_initial():
    plt.figure(figsize=(12, 8))
    sns.countplot(y='SUBJECT', hue='LOCATION', data=crop_production_data, palette='viridis')
    plt.title('Distribution of Crop Yield by Location')
    plt.xlabel('Count')
    plt.ylabel('Crop Type')
    plt.legend(title='Location', loc='upper right')
    plt.savefig('problem_5_1_initial.png')
    plt.show()

problem_5_1_initial()


average_production_by_country = crop_production_data.groupby('LOCATION')['Value'].mean()

selected_locations = average_production_by_country.sort_values(ascending=False).head(7).index.tolist()

filtered_data = crop_production_data[crop_production_data['LOCATION'].isin(selected_locations)]

def problem_5_1_adjusted():
    plt.figure(figsize=(12, 8))
    sns.countplot(y='SUBJECT', hue='LOCATION', data=filtered_data, palette='viridis')
    plt.title('Distribution of Crop Yield by Selected Locations')
    plt.xlabel('Count')
    plt.ylabel('Crop Type')
    plt.legend(title='Location', loc='upper right')
    plt.savefig('problem_5_1_adjusted.png')
    plt.show()

problem_5_1_adjusted()

