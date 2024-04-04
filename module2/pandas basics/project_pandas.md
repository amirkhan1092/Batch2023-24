
1. **Data Manipulation & Aggregation:**
   
   Description: You're provided with a DataFrame containing sales data with columns 'Date', 'Product', and 'Revenue'. Write a function to find the top 3 selling products for each month along with their total revenue.
   
   Example:
   ```python
   import pandas as pd

   # Sample DataFrame
   data = {'Date': ['2024-01-01', '2024-01-05', '2024-02-02', '2024-02-15'],
           'Product': ['A', 'B', 'A', 'C'],
           'Revenue': [100, 200, 150, 120]}
   df = pd.DataFrame(data)

   # Function to find top 3 selling products for each month
   def top_selling_products(df):
       df['Date'] = pd.to_datetime(df['Date'])
       df['Month'] = df['Date'].dt.to_period('M')
       top_products = df.groupby(['Month', 'Product']).sum()
       top_products = top_products.groupby('Month').apply(lambda x: x.nlargest(3, 'Revenue'))
       return top_products

   print(top_selling_products(df))
   ```

2. **Data Transformation:**

   Description: Write a function that takes a DataFrame with a column of timestamps and returns a new DataFrame with an additional column indicating the time difference (in seconds) between consecutive timestamps.
   
   Example:
   ```python
   import pandas as pd

   # Sample DataFrame
   data = {'Timestamp': ['2024-01-01 12:00:00', '2024-01-01 12:01:00', '2024-01-01 12:05:00']}
   df = pd.DataFrame(data)

   # Function to calculate time difference
   def calculate_time_difference(df):
       df['Timestamp'] = pd.to_datetime(df['Timestamp'])
       df['Time_Difference'] = df['Timestamp'].diff().dt.total_seconds()
       return df

   print(calculate_time_difference(df))
   ```

3. **Missing Data Handling:**

   Description: Given a DataFrame with missing values, implement a function to impute missing values in a specific column using linear interpolation, considering the values in adjacent rows.
   
   Example:
   ```python
   import pandas as pd

   # Sample DataFrame
   data = {'Value': [1, None, 3, None, 5]}
   df = pd.DataFrame(data)

   # Function to impute missing values using linear interpolation
   def interpolate_missing_values(df):
       df['Value'] = df['Value'].interpolate(method='linear')
       return df

   print(interpolate_missing_values(df))
   ```

4. **Multi-indexing & Reshaping:**

   Description: Transform a given DataFrame into a multi-index DataFrame with indices as 'Year' and 'Month', columns as 'Product', and values as the sum of 'Revenue'. Then, stack the resulting DataFrame and sort by the total revenue.
   
   Example:
   ```python
   import pandas as pd

   # Sample DataFrame
   data = {'Date': ['2024-01-01', '2024-01-05', '2024-02-02', '2024-02-15'],
           'Product': ['A', 'B', 'A', 'C'],
           'Revenue': [100, 200, 150, 120]}
   df = pd.DataFrame(data)

   # Function to transform DataFrame
   def transform_dataframe(df):
       df['Date'] = pd.to_datetime(df['Date'])
       df.set_index('Date', inplace=True)
       multi_index_df = df.groupby([df.index.year, df.index.month, 'Product']).sum().unstack()
       multi_index_df = multi_index_df.stack().sort_values(ascending=False)
       return multi_index_df

   print(transform_dataframe(df))
   ```

5. **GroupBy & Filtering:**

   Description: Given a DataFrame with columns 'City', 'Product', and 'Revenue', write a function to filter out the cities where the total revenue for any product exceeds the median revenue across all cities.
   
   Example:
   ```python
   import pandas as pd

   # Sample DataFrame
   data = {'City': ['A', 'B', 'A', 'B'],
           'Product': ['X', 'X', 'Y', 'Y'],
           'Revenue': [100, 200, 150, 300]}
   df = pd.DataFrame(data)

   # Function to filter cities based on revenue
   def filter_cities(df):
       median_revenue = df.groupby('City')['Revenue'].median()
       cities_to_keep = median_revenue[median_revenue >= df['Revenue'].median()].index
       filtered_df = df[df['City'].isin(cities_to_keep)]
       return filtered_df

   print(filter_cities(df))
   ```

6. **Time Series Analysis:**

   Description: Implement a function to calculate the rolling average of a time series data stored in a DataFrame, considering a window size of 30 days. Then, identify the top 3 peaks and valleys in the smoothed time series data.
   
   Example:
   ```python
   import pandas as pd

   # Sample DataFrame
   data = {'Date': pd.date_range(start='2024-01-01', periods=100),
           'Value': [i ** 2 for i in range(100)]}
   df = pd.DataFrame(data)

   # Function to calculate rolling average and find peaks and valleys
   def analyze_time_series(df):
       df['Rolling_Avg'] = df['Value'].rolling(window=30).mean()
       df['Diff'] = df['Rolling_Avg'].diff()
       peaks = df.nlargest(3, 'Diff')['Date']
       valleys = df.nsmallest(3, 'Diff')['Date']
       return peaks, valleys

   peaks, valleys = analyze_time_series(df)
   print("Peaks:", peaks)
   print("Valleys:", valleys)
   ```

7. **Merge & Join Operations:**

   Description: Given two DataFrames - one with customer information ('Customer_ID', 'Name', 'Email') and the other with purchase history ('Customer_ID', 'Product', 'Purchase_Date'), write a function to create a merged DataFrame containing the most recent purchase for each customer.
   
   Example:
   ```python
   import pandas as pd

   # Sample DataFrames
   customers = {'Customer_ID': [1, 2],
                'Name': ['Alice', 'Bob'],
                'Email': ['alice@example.com', 'bob@example.com']}
   purchases = {'Customer_ID': [1, 1, 2],
                'Product': ['A', 'B', 'C'],
                'Purchase_Date': ['2024-01-01', '2024-02-01', '2024-03-01']}
   customers_df = pd.DataFrame(customers)
   purchases_df = pd.DataFrame(purchases)

   # Function to merge DataFrames and find most recent purchase
   def recent_purchase(df1, df2):
       merged_df = pd.merge(df1, df2, on='Customer_ID')
       merged_df['Purchase_Date'] = pd.to_datetime(merged_df

['Purchase_Date'])
       recent_purchase_df = merged_df.groupby('Customer_ID').apply(lambda x: x.nlargest(1, 'Purchase_Date')).reset_index(drop=True)
       return recent_purchase_df

   print(recent_purchase(customers_df, purchases_df))
   ```

8. **Handling Categorical Data:**

   Description: Write a function to encode categorical variables in a DataFrame using one-hot encoding, considering only the top 10 most frequent categories for each column.
   
   Example:
   ```python
   import pandas as pd

   # Sample DataFrame
   data = {'Category': ['A', 'B', 'C', 'A', 'B', 'D', 'E', 'F', 'G', 'H', 'I', 'J']}
   df = pd.DataFrame(data)

   # Function to perform one-hot encoding
   def one_hot_encoding(df):
       top_categories = df['Category'].value_counts().nlargest(10).index
       encoded_df = pd.get_dummies(df[df['Category'].isin(top_categories)], columns=['Category'])
       return encoded_df

   print(one_hot_encoding(df))
   ```

9. **Advanced Indexing:**

   Description: Implement a function that selects rows from a DataFrame based on a complex condition involving multiple columns and logical operators, ensuring efficient performance for large datasets.
   
   Example:
   ```python
   import pandas as pd

   # Sample DataFrame
   data = {'A': [1, 2, 3, 4, 5],
           'B': [6, 7, 8, 9, 10]}
   df = pd.DataFrame(data)

   # Function to perform advanced indexing
   def advanced_indexing(df):
       filtered_df = df[(df['A'] > 2) & (df['B'] < 9)]
       return filtered_df

   print(advanced_indexing(df))
   ```

10. **Performance Optimization:**

    Description: Given a DataFrame containing stock price data with columns 'Date', 'Symbol', and 'Price', optimize the computation of the percentage change in price for each symbol over a rolling window of 30 days to minimize memory usage and execution time.
   
    Example:
    ```python
    import pandas as pd

    # Sample DataFrame
    data = {'Date': pd.date_range(start='2024-01-01', periods=100),
            'Symbol': ['AAPL'] * 50 + ['GOOG'] * 50,
            'Price': [100.0 + i for i in range(100)]}
    df = pd.DataFrame(data)

    # Function to compute percentage change efficiently
    def compute_percentage_change(df):
        df['Percentage_Change'] = df.groupby('Symbol')['Price'].transform(lambda x: x.pct_change(periods=30))
        return df

    print(compute_percentage_change(df))
    ```

These examples should give a comprehensive understanding of the complexities and applications of Pandas in real-world scenarios.