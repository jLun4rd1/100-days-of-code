#==================================================|
#|----|----|----|----|----|----|----|----|----|----|
## Too hard to clean and read!
# with open('weather_data.csv') as data_file:
#     data = data_file.readlines()
    
# for item in data:
#     item = item.strip('\n')
#     print(item)
#|----|----|----|----|----|----|----|----|----|----|
#==================================================|

#==================================================|
#|----|----|----|----|----|----|----|----|----|----|
## Too many lines to write!!
# import csv 

# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
#|----|----|----|----|----|----|----|----|----|----|
#==================================================|

#==================================================|
#|----|----|----|----|----|----|----|----|----|----|
## Now that's the way to go!!!
# import pandas as pd

# data = pd.read_csv("weather_data.csv")
# print(data["temp"])
#|----|----|----|----|----|----|----|----|----|----|
#==================================================|

#==================================================|
#|----|----|----|----|----|----|----|----|----|----|
## We're on it !!!!
import pandas as pd

# data = pd.read_csv("weather_data.csv")
# # print(type(data))
# # print(type(data["temp"]))

# data_dict = data.to_dict()
# # print(data_dict)
#|----|----|----|----|----|----|----|----|----|----|
#==================================================|

#==================================================|
#|----|----|----|----|----|----|----|----|----|----|
# # Hard way to calculate average
# temp_list = data['temp'].to_list()
# temp_sum = sum(temp_list)
# temp_avg = temp_sum / len(temp_list)
# print(f"Hard way: {round(temp_avg, 2)}")

# # Pandas' way to calculate average!!
# pandas_temp_avg = data['temp'].mean()
# print(f"Pandas' way: {round(pandas_temp_avg, 2)}")

# pandas_temp_max = data['temp'].max()
# print(f'Max: {pandas_temp_max}')
#|----|----|----|----|----|----|----|----|----|----|
#==================================================|

#==================================================|
#|----|----|----|----|----|----|----|----|----|----|
# # Get Data in Columns
# print(data['condition'])
# # OR
# print(data.condition)

# # Get Data in Rows
# print(data[data['day'] == 'Monday'])

# # Getting data where the temperature was equals to the max temperature
# print(data[data['temp'] == pandas_temp_max])

# monday = data[data["day"] == 'Monday']
# monday_temp_in_farenheit = (monday.temp * 9 / 5) + 32
# print(monday_temp_in_farenheit)
#|----|----|----|----|----|----|----|----|----|----|
#==================================================|

# Create a DataFrame from scratch
data_dict = {
    "students": ['A','B','C'],
    "scores": [1, 2, 3]
}
data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv")