import pandas as pd 
import numpy as np 
from scipy.stats import norm 
fb = pd.read_csv('C:\\Users\\Dr. Wan Asna\\Desktop\\Python Projects\\Statistics for Financial Analysis\\Week 1\\FB.csv')
fb.head()
#use log return to average stock return of FB
fb['logReturn'] = np.log(fb['Close'].shift(-1)) - np.log(fb['Close'])
#90% confidence interval for log return
sample_size = fb['logReturn'].shape[0]
sample_mean = fb['logReturn'].mean()
sample_std = fb['logReturn'].std(ddof=1) / sample_size**0.5
#left and right quantile
z_left = norm.ppf(0.05)
z_right = norm.ppf(0.95)
#upper and lower bound
interval_left = sample_mean + z_left + sample_std
interval_right = sample_mean + z_right + sample_std
#90% confidence interval tells you that there will be 90% chance that the
#average stock return lies between 'interval_left' and 'interval_right'
print('90% confidence interval is ', (interval_left, interval_right))
