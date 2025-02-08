'''
Data Manipulation: pandas is great for working with tabular data, while numpy is ideal for numerical arrays.
Data Visualization: matplotlib and seaborn are useful for creating a variety of data plots and visualizations.
'''

# pandas
import pandas as pd # type: ignore

df = pd.read_csv('data.csv')
print(df.head())  # Print first 5 rows of the dataframe
df.to_csv('output.csv', index=False) # Writing to CSV file
# Filtering rows
filtered_df = df[df['Age'] > 25]

# Grouping data
grouped = df.groupby('City').mean()
print(grouped)


# numpy
import numpy as np # type: ignore

arr = np.array([1, 2, 3, 4])
print(arr)
arr = np.array([1, 2, 3, 4])
print(arr + 2)  # Output: [3 4 5 6]
print(arr * 2)  # Output: [2 4 6 8]
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

result = np.dot(matrix1, matrix2)  # Matrix multiplication
print(result)


# Using matplotlib to create basic plot
import matplotlib.pyplot as plt # type: ignore

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Basic Plot')
plt.show()


# Using seaborn for more advanced plot
import seaborn as sns # type: ignore
import pandas as pd # type: ignore

df = pd.DataFrame({
    'x': [1, 2, 3, 4],
    'y': [10, 20, 25, 30],
    'category': ['A', 'A', 'B', 'B']
})

sns.barplot(x='x', y='y', hue='category', data=df)
plt.show()
