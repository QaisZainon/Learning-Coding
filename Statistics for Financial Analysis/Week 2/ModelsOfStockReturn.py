import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

fb = pd.read_csv('C:\\Users\\Dr. Wan Asna\\Desktop\\Coding Projects\\Statistics for Financial Analysis\\Week 1\\FB.csv')
fb.head()
#Playing around ms data by calculating the log daily return
fb['LogReturn'] = np.log(fb['Close']).shift(-1) - np.log(fb['Close'])
#Plot a histogram to show the distribution of log return of Microsoft
#You can see it is very close to a normal distribution
#import function severly outdated
from scipy.stats import norm
mu = fb['LogReturn'].mean()
sigma = fb['LogReturn'].std(ddof=1)

density = pd.DataFrame()
density['x'] = np.arange(fb['LogReturn'].min() - 0.01, fb['LogReturn'].max() + 0.01, 0.001)
density['pdf'] = norm.pdf(density['x'], mu, sigma)

fb['LogReturn'].hist(bins=50, figsize=(15, 8))
plt.plot(density['x'], density['pdf'], color='red')
plt.show()

#probability that the stock price of microsoft will drop over 5% in a day
prob_return1 = norm.cdf(-0.05, mu, sigma)
print('The Probability is ', prob_return1)
#drop over 40% in 220 days
mu220 = 220*mu
sigma220 = (220**0.5) * sigma
print('The probability of dropping over 40% in 220 days is ', norm.cdf(-0.4, mu220, sigma220))

#Value at risk(VaR)
VaR = norm.ppf(0.05, mu, sigma)
print('Single day value at risk ', VaR)
#Quantile
#5% quantile
print('5% quantile ', norm.ppf(0.05, mu, sigma))
#95% quantile
print('95% quantile ', norm.ppf(0.95, mu, sigma))
#legit no fucking clue lmaooooo