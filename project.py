import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import matplotlib.pyplot as plt
import numpy as np

# Define the ticker symbol
tickerSymbol = 'NKE'

# Get data for this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
startDate = datetime(2023, 12, 1)
endDate = datetime.now()

# Get historical data
tickerDf = tickerData.history(period='1d', start=startDate, end=endDate)

# Select only the 'Close' column
tickerDf = tickerDf[['Close']]

# Rename the 'Close' column to 'Price'
tickerDf = tickerDf.rename(columns={'Close': 'Price'})

# Add a new column for the stock name
tickerDf['Name'] = tickerSymbol

# Reset the index to move the date into a column
tickerDf.reset_index(inplace=True)

# Convert the 'Date' column to string and remove the time
tickerDf['Date'] = tickerDf['Date'].dt.strftime('%Y-%m-%d')

# Save the dataframe to a csv file
tickerDf.to_csv('stock_data.csv', index=False)

# Load the data from the CSV file
df = pd.read_csv('stock_data.csv')

# Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Add a new column 'DateOrd' that represents the date as an ordinal number
df['DateOrd'] = df['Date'].apply(lambda x: x.toordinal())

# Define the feature (independent variable) and the target (dependent variable)
X = df['DateOrd'].values.reshape(-1,1)
y = df['Price'].values.reshape(-1,1)

# Split the data into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train the model
model = LinearRegression()  
model.fit(X_train, y_train)
# Make predictions using the test set
y_pred = model.predict(X_test)

# Compare actual output values with predicted values
df_compare = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
print(df_compare)

# Predict the stock price for the next month
next_month = np.array([df['DateOrd'].max() + i for i in range(1, 31)]).reshape(-1, 1)
predicted_prices = model.predict(next_month)

# Print the predicted prices
for i in range(30):
    print(f"Day {i+1}: {predicted_prices[i][0]}")

# You can also plot the actual vs predicted prices
plt.scatter(X_test, y_test,  color='gray')
plt.plot(X_test, y_pred, color='red', linewidth=2)
plt.show()
