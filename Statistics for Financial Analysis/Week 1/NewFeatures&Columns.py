import pandas as pd 
import matplotlib.pyplot as plt 
fb = pd.read_csv('C:\\Users\\Dr. Wan Asna\\Desktop\\Coding Projects\\Statistics for Financial Analysis\\Week 1\\FB.csv')
#Create a new column PriceDiff in DataFrame fb
fb['PriceDiff'] = fb['Close'].shift(-1) - fb['Close']
#Create a new column Return in the DataFrame fb
fb['Return'] = fb['PriceDiff'] /fb['Close']
#New column Direction that denotes 1 or 0 based on PriceDiff's value for all records
fb['Direction'] = [1 if fb['PriceDiff'].loc[ei] > 0 else 0 for ei in fb.index]
print('Price difference on {} is {}. return is {}. direction is {}'.format('2019-06-06', fb.loc[0, 'PriceDiff'], fb.loc[0, 'Return'], fb.loc[0, 'Direction']))
#Moving average for 50 days 
fb['MA10'] = fb['Close'].rolling(10).mean()
fb['MA50'] = fb['Close'].rolling(50).mean()
#plot the moving average
plt.figure(figsize=(10, 8))
#fb.loc['2019-06-06':'2020-06-05', 'MA50'].plot(label='MA50')
#fb.loc['2019-06-06':'2020-06-05', 'Close'].plot(label='Close')
#plt.legend()
ax = plt.gca()
fb.plot(kind='line', x='Date', y='MA10', color='blue', ax=ax)
fb.plot(kind='line', x='Date', y='MA50', color='red', ax=ax)
fb.plot(kind='line', x='Date', y='Close', color='green', ax=ax)
plt.xticks(rotation=45) #makes the x axis diagonal
plt.show()