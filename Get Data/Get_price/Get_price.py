import yfinance as yf
import pandas as pd
import numpy as np

# Get historical data for EUR/USD
eur_usd_data = yf.download("EUR=X", interval = "5m", start="2010-01-01", end="2010-01-07")

# Calculate the moving average
eur_usd_data['MA'] = eur_usd_data['Close'].rolling(window=14).mean()

# Calculate the Bollinger Bands
eur_usd_data['STD'] = eur_usd_data['Close'].rolling(window=14).std()
eur_usd_data['Upper_Band'] = eur_usd_data['MA'] + (eur_usd_data['STD'] * 2)
eur_usd_data['Lower_Band'] = eur_usd_data['MA'] - (eur_usd_data['STD'] * 2)

# Calculate the RSI
delta = eur_usd_data['Close'].diff()
gain = delta.where(delta > 0, 0)
loss = -delta.where(delta < 0, 0)
avg_gain = gain.rolling(window=14).mean()
avg_loss = loss.rolling(window=14).mean()
rs = avg_gain / avg_loss
eur_usd_data['RSI'] = 100 - (100 / (1 + rs))

# Calculate the ADX
up = eur_usd_data['Close'].diff()
down = eur_usd_data['Close'].diff()
up[up < 0] = 0
down[down > 0] = 0

pos_move = pd.Series(up)
neg_move = pd.Series(down)

#Calculating the +DM and -DM
pos_move[0] = 0
neg_move[0] = 0

for i in range(1, len(eur_usd_data)):
    if eur_usd_data['Close'][i] - eur_usd_data['Close'][i - 1] > 0:
        pos_move[i] = eur_usd_data['Close'][i] - eur_usd_data['Close'][i - 1]
    else:
        pos_move[i] = 0
    if eur_usd_data['Close'][i - 1] - eur_usd_data['Close'][i] > 0:
        neg_move[i] = eur_usd_data['Close'][i - 1] - eur_usd_data['Close'][i]
    else:
        neg_move[i] = 0

#Calculating the +DI and -DI
pos_DI = pos_move.rolling(window=14).mean()
neg_DI = neg_move.rolling(window=14).mean()

dx = pd.Series((pos_DI - neg_DI) / (pos_DI + neg_DI))
adx = dx.rolling(window=14).mean()
eur_usd_data['ADX'] = adx

print(eur_usd_data)
with pd.ExcelWriter('USA_economy_headlines.xlsx',mode='a') as writer:  
    eur_usd_data.to_excel(writer,index=False,)
print("The data has been saved to an excel file")