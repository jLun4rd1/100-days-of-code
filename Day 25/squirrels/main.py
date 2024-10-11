import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241011.csv")

# Pandas' solution!
summarized_data = data.groupby(['Primary Fur Color'])['Unique Squirrel ID'].count()

# My solution!
final_dict = {
    'Fur Color': [],
    'Count': []
}

colors = data['Primary Fur Color'].drop_duplicates().dropna().to_list()

for color in colors:
    color_data = data[data['Primary Fur Color'] == f'{color}']['Unique Squirrel ID']
    color_count = color_data.count()
    final_dict['Fur Color'].append(color.lower())
    final_dict['Count'].append(color_count)

final_df = pd.DataFrame(final_dict)
# final_df.to_csv('squirrel_count.csv)