

1. **Load Data and Basic Operations:**
```python
import pandas as pd

# Load CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Display the first 5 rows of the DataFrame
print(df.head())

# Display column names
print(df.columns)

# Check shape
print(df.shape)

# Data types of each column
print(df.dtypes)
```

2. **Data Selection and Filtering:**
```python
# Select a single column
single_column = df['column_name']

# Select multiple columns
multiple_columns = df[['column1', 'column2']]

# Filter rows based on a condition
filtered_data = df[df['column'] > 100]
```

3. **Data Cleaning:**
```python
# Check for missing values
print(df.isnull().sum())

# Replace missing values with mean
df.fillna(df.mean(), inplace=True)

# Drop rows with missing values
df.dropna(inplace=True)

# Drop unnecessary columns
df.drop(['unnecessary_column'], axis=1, inplace=True)
```

4. **Data Manipulation:**
```python
# Create a new column
df['new_column'] = df['column1'] + df['column2']

# Apply a function to a column
df['column'] = df['column'].apply(lambda x: x.lower())

# Sort the DataFrame based on a column
df.sort_values(by='column', inplace=True)

# Group data and perform aggregation
grouped_data = df.groupby('group_column').agg({'numeric_column': 'sum'})
```

5. **Data Visualization:**
```python
import matplotlib.pyplot as plt
import seaborn as sns

# Histogram
df['numeric_column'].hist()
plt.show()

# Bar chart
sns.countplot(x='categorical_column', data=df)
plt.show()

# Line chart
df.plot(x='date_column', y='numeric_column')
plt.show()
```

6. **Data Analysis:**
```python
# Descriptive statistics
print(df.describe())

# Most frequent value
print(df['categorical_column'].value_counts().idxmax())

# Correlation
print(df.corr())

# Cross-tabulation
print(pd.crosstab(df['column1'], df['column2']))
```

7. **Data Transformation:**
```python
# Convert categorical column into dummy variables
dummy_variables = pd.get_dummies(df['categorical_column'])

# Apply one-hot encoding
encoded_data = pd.get_dummies(df)

# Binning numerical data
df['binned_column'] = pd.cut(df['numeric_column'], bins=3)

# Normalize numerical data
df['normalized_column'] = (df['numeric_column'] - df['numeric_column'].min()) / (df['numeric_column'].max() - df['numeric_column'].min())
```

8. **Combining DataFrames:**
```python
# Merge DataFrames
merged_df = pd.merge(df1, df2, on='common_column')

# Concatenate DataFrames
concatenated_df = pd.concat([df1, df2], axis=0)  # along rows
concatenated_df = pd.concat([df1, df2], axis=1)  # along columns

# Join DataFrames
joined_df = df1.join(df2, how='inner')
```
