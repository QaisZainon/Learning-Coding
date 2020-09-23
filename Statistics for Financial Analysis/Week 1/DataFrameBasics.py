#! python3
#import the packages 'Pandas' and 'MatPlotLib' into python
import pandas as pd 
import matplotlib.pyplot as plt 
#import Facebook's stock stock data
#corsera's code is obsolete as DataFrame not having the particular function as well as find_csv no longer supported
fb = pd.read_csv('C:\\Users\\Dr. Wan Asna\\Desktop\\Python Projects\\Statistics for Financial Analysis\\Week 1\\FB.csv')
#prints the first five rows
print(fb.head())
#prints the size of the data frame
print(fb.shape)
#print summary statistics of Facebook
print(fb.describe())
#select all the price information of facebook in 2019-2020, index was never specified in the tutorial
fb_2019 = fb.loc['0':'252']
#print the price of facebook on '2020-01-13', coursera was wrong again as the argument presented was incorrect, output was incorrect as well
print(fb_2019.loc['152':'152'])
#print the opening price of the first row, index not specified
print(fb.iloc[0, 1])
#Plot stock data using plot() method, horrible, index is default, never specified to define date as index
plt.figure(figsize=(10,8))
#fb['Close'].plot() #The line that was taught to input
ax = plt.gca() #gca stands for 'get current axis'
fb.plot(kind='line', x='Date', y='Low', color='red', ax=ax)
fb.plot(kind='line', x='Date', y='High', color='green', ax=ax)
fb.plot(kind='line', x='Date', y='Close', color='black', ax=ax)
plt.show()
