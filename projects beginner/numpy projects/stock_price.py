import numpy as np
import matplotlib.pyplot as plt

# Sample historical stock prices (replace with actual data)
# Here, we use random data for demonstration purposes
dates = np.array(['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'])
prices = np.array([100, 102, 98, 105, 110])

# Calculate simple moving average (SMA)
window_size = 3  # Adjust the window size as needed
sma = np.convolve(prices, np.ones(window_size)/window_size, mode='valid')

# Plot stock prices over time
plt.figure(figsize=(10, 6))
plt.plot(dates, prices, label='Stock Price', marker='o')
plt.plot(dates[window_size - 1:], sma, label='Simple Moving Average', linestyle='--')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Stock Market Analysis')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
