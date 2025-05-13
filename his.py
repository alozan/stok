import yfinance as yf
import matplotlib.pyplot as plt

data = yf.download ("PLTR.MX", start="2024-08-25", end="2025-05-12")
print(data.head())
print(data.tail())

data['Close'].plot()
plt.title("Stock")
plt.show()
