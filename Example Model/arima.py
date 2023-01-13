import pandas as pd
from statsmodels.tsa.arima_model import ARIMA

# Load data from Excel spreadsheet
data = pd.read_excel("forex_data.xlsx")

# Convert data to a time series
ts = data["Exchange Rate"]

# Fit the ARIMA model
model = ARIMA(ts, order=(2, 1, 0))
model_fit = model.fit()

# Make predictions
forecast = model_fit.forecast(steps=30)[0]