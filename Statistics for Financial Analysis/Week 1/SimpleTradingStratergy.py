#! python3
import pandas as pd 
import matplotlib.pyplot as plt 
#import FB's stock data, add two columns - MA10 and MA50
#use dropna to remove any " Not a Number" data
fb = pd.read_csv('C:\\Users\\Dr. Wan Asna\\Desktop\\Coding Projects\\Statistics for Financial Analysis\\Week 1\\FB.csv')
fb['MA10'] = fb['Close'].rolling(10).mean()
fb['MA50'] = fb['Close'].rolling(50).mean()
fb = fb.dropna()
#Add a new column 'Shares', if MA10 > MA50, denote as 1 (long one share of stock), otherwise denote as 0 (do nothing)
fb['Shares'] = [1 if fb.loc[ei, 'MA10']>fb.loc[ei, 'MA50'] else 0 for ei in fb.index]
#Add a new column 'Profit' using List Comprehension, for any rows in fb, if Shares=1, the profit is calculated as the close price of
#tomorrow - the close price of today. Otherwise the profit is 0
#Plot a graph to show the Profit/Loss
fb['Close1'] = fb['Close'].shift(-1)
fb['Profit'] = [fb.loc[ei, 'Close1'] - fb.loc[ei, 'Close'] if fb.loc[ei, 'Shares']==1 else 0 for ei in fb.index]
fb['Profit'].plot()
plt.axhline(y=0, color='red')
plt.show()
#Use. cumsum() to calculate the accumulated wealth over the period
fb['wealth'] = fb['Profit'].cumsum()
fb['wealth'].plot()
plt.title('Total money you win is {}'.format(fb.loc[fb.index[-2], 'wealth']))
plt.show()