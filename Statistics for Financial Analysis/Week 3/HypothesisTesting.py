import pandas as pd 
import numpy as np 
from scipy.stats import norm 
import matplotlib.pyplot as plt 
#import facebook.csv, and add a new feature - logreturn
fb = pd.read_csv('C:\\Users\\Dr. Wan Asna\\Desktop\\Python Projects\\Statistics for Financial Analysis\\Week 1\\FB.csv')
fb['logReturn'] = np.log(fb['Close'].shift(-1)) - np.log(fb['Close'])
#Log return goes up and down during the period
fb['logReturn'].plot(figsize = (20, 8))
plt.axhline(0, color = 'red')
plt.show()
#Testing a claim by hypothesis testing
'''Step 1 = Setting up a hypothesis'''
#H0 means average stock return is 0 
#H1 means average stocks is not equal to 0
'''Step 2 = Calculate test statistic'''
sample_mean = fb['logReturn'].mean()
sample_std = fb['logReturn'].std(ddof=1)
n = fb['logReturn'].shape[0]
#if sample size n is large enough, we can use z-distribution, instead of t-distribution
#mu = 0 under the null hypothesis
zhat = (sample_mean - 0)/(sample_std/n**0.5) #I honestly dont know this 
print(zhat)
'''Step 3 = Set decision criteria'''
#confidence level
alpha = 0.05
z_left = norm.ppf(alpha/2, 0, 1)
z_right = -z_left #z-distribution is symmetric
print(z_left, z_right)
'''Step 4 = Make decision -should we reject H0 ?'''
print('At significant level of {}, shall we reject: {}'.format(alpha, zhat > z_right or zhat < z_left))
