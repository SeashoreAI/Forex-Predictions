# Forex Predictions
Make accurate multi-factor forex prediction using multiple factors           
5 day prediction          
## Data Gathering
Gather the neccesary data in order to train the project
1 year worth of data will be used in order to train our models
### Sociological Indicators (LSTM)
**News**             
1.Political        
2.Sociological              
3.Economical News 
**Time Periods**    
1/2/3/5/10 day      
Use of https://newscatcherapi.com/api
### Short Term Economic Indicators(ARIMA)
1.Moving Averages     
2.Relative Strength Index (RSI)      
3.Stochastics          
4.Average Directional Movement (ADX)          
5.Bollinger Bands                
**Time Periods**    
15min/30min/2hour/1day/3days/7days/14days   
### Short Term Stock Indicators (LSTM)
1. S/P 500     
  Moving Averages    
  Relative Strength Index (RSI)        
  Stochastics          
  Average Directional Movement (ADX)           
  Bollinger Bands          
2. FTSEurofirst 300 Index     
  Moving Averages          
  Relative Strength Index (RSI)  
  Stochastics 
  Average Directional Movement (ADX) 
  Bollinger Bands     

**Time Periods**
15min/30min/2hour/1day/3days/7days/14days   
## Data Combination
All the data combined from the 3 models will end up in a final ARIMA model
