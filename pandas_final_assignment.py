# Q1: Write a code to print the data present in the second row of the dataframe, df.
import pandas as pd
course_name = ['Data Science', 'Machine Learning', 'Big Data', 'Data Engineer']
duration = [2, 3, 6, 4]
df = pd.DataFrame(data={'course_name': course_name, 'duration': duration})
print(df.iloc[1])
print("\n")
"""Q2: What is the difference between the functions loc and iloc in pandas.DataFrame?
loc: Access rows and columns by labels or a boolean array.
iloc: Access rows and columns by integer-based index positions."""

# Q3: Reindex the dataframe and find the output for new_df.loc[2] and new_df.iloc[2]
reindex = [3, 0, 1, 2]
new_df = df.reindex(reindex)

# Outputs
print("new_df.loc[2]:")
print(new_df.loc[2])  

print("new_df.iloc[2]:")
print(new_df.iloc[2])
print("\n")

"""Q4. Write a code to find the following statistical measurements for the above dataframe df1:
(i) mean of each and every column present in the dataframe.
(ii) standard deviation of column, ‘column_2’"""
import numpy as np

columns = ['column_1', 'column_2', 'column_3', 'column_4', 'column_5', 'column_6']
indices = [1, 2, 3, 4, 5, 6]
df1 = pd.DataFrame(np.random.rand(6, 6), columns=columns, index=indices)
print(df1.mean())
print(df1['column_2'].std())
print("\n")

"""Q5 : Replace the data present in the second row of column, ‘column_2’ by a string variable then find the
mean of column, column_2.
If you are getting errors in executing it then explain why."""
# Replacing second row of column_2 with a string
df1.loc[2, 'column_2'] = 'text'
try:
    print(df1['column_2'].mean())
except TypeError as e:
    print("Error :",)
print("\n")
# Explanation: Mean cannot be calculated because the column contains a non-numeric value.

"""Q6: Windows function in pandas and types.
Windows functions in pandas perform operations over a sliding window of rows. Types include:

Rolling: For moving averages or sums.
Expanding: Cumulative calculations.
EWM (Exponentially Weighted Mean): Weighted moving averages."""
# Rolling mean
print(df1['column_1'].rolling(window=3).mean())
print("\n")

# Q8: Calculate the difference between two dates in days, hours, and minutes.
from datetime import datetime
# Input two dates
date1 = input("Enter the first date (YYYY-MM-DD): ")
date2 = input("Enter the second date (YYYY-MM-DD): ")
# Convert to datetime
date1 = pd.to_datetime(date1)
date2 = pd.to_datetime(date2)
# Calculate difference
delta = date2 - date1
days = delta.days
hours = delta.total_seconds() // 3600
minutes = delta.total_seconds() // 60
print(f"Difference: {days} days, {hours} hours, {minutes} minutes")
print("\n")

# Q9: Convert a column to categorical data type and display sorted data.
file_path = input("Enter the file path: ")
column_name = input("Enter the column name to convert: ")
categories = input("Enter category order (comma-separated): ").split(',')
df = pd.read_csv(file_path)
# Convert to categorical
df[column_name] = pd.Categorical(df[column_name], categories=categories, ordered=True)
# Display sorted data
print(df.sort_values(by=column_name))
print("\n")

# Q10: Visualize sales data with a stacked bar chart.
import matplotlib.pyplot as plt
file_path = input("Enter the sales data file path: ")
df = pd.read_csv(file_path)
# Assuming columns: 'Product', 'Category', 'Sales', 'Date'
df['Date'] = pd.to_datetime(df['Date'])
df_pivot = df.pivot_table(values='Sales', index='Date', columns='Category', aggfunc='sum')
# Plot
df_pivot.plot(kind='bar', stacked=True)
plt.title('Sales by Product Category Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()
print("\n")

# Q11: Calculate mean, median, and mode of student test scores.
import pandas as pd

file_path = input("Enter the file path of the CSV file: ")
df = pd.read_csv(file_path)

# Calculate statistics
mean = df['Test Score'].mean()
median = df['Test Score'].median()
mode = df['Test Score'].mode().tolist()
results = pd.DataFrame({
    'Statistic': ['Mean', 'Median', 'Mode'],
    'Value': [round(mean, 2), round(median, 2), ", ".join(map(str, mode))]
})
print(results)
