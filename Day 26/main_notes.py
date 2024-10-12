import random

numbers = [1,2,3]

# For Loops - 4 lines!
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
print('For Loop: ', new_list)

## List comprehension - 1 single life-saving line!
# Sintax -> [new_item for item in list]
new_list = [n + 1 for n in numbers]
print('List comprehension: ', new_list)

# Exercise 1:
name = 'João'
new_list = [letter for letter in name]
print("Name's list: ", new_list)

# Exercise 2:
new_list = [n*2 for n in range(1, 5)]
print("Doubled numbers: ", new_list)

## Conditional List Comprehension
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name) <= 4]
long_names = [name.upper() for name in names if len(name) >= 5]
print('Only short names: ', short_names)
print('Upper long names: ', long_names)

## Dictionary Comprehension - Holy Moses!
# Syntax -> {new_key:new_value for item in list}
# Syntax -> {new_key:new_value for (key, value) in dict.items()}
# Syntax -> {new_key:new_value for (key, value) in dict.items() if condition}
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
students_scores = {name:random.randint(1, 100) for name in names}
passed_students = {name:score for (name, score) in students_scores.items() if score >= 60}
print("Student's scores: ", students_scores)
print("Passed students: ", passed_students)

## Pandas Comprehension !!!!!
# Syntax -> {new_key:new_value for (index, row) in df.iterrows()}
import pandas as pd
passed_students = {
    'Name': ['Alex', 'Beth', 'Caroline'],
    'Score': [60, 70, 80]
}
passed_students_df = pd.DataFrame(passed_students)
print('Passed students DataFrame:\n', passed_students_df)

## Looping through a DataFrame
# for (key, value) in passed_students_df.items():
    # print(key) >> Name of Columns
    # print(value) >> Value of each Column (Will print only the column's content, one column at a time)

## Looping through ROWS of a DataFrame
for (index, row) in passed_students_df.iterrows():
    # print(row.Name) # >> Rows will be returned as Series, so it has attributes. For exemple: row.Name or row.Score
    if row.Name == 'Alex':
        print(row.Score)
        
## ====================================================== ##      
## Notes from teacher:
import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
## ====================================================== ##  