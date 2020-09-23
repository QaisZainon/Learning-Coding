import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import norm 
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
#Sample mean and SD keep changing, but always within a certain range
Fstsample = pd.DataFrame(np.random.normal(10, 5, size=30))
print('sample mean is ', Fstsample[0].mean())
print('sample SD is ', Fstsample[0].std(ddof = 1))
#Fstsample.hist(density=True, bins=100, figsize=(15,8))
#plt.show()
#Empirical Distribution of mean
meanlist = []
for t in range(10000):
    sample = pd.DataFrame(np.random.normal(10, 5, size=30))
    meanlist.append(sample[0].mean())
collection = pd.DataFrame()
collection['meanlist'] = meanlist
logging.debug(collection)
#similarly the syllabus was not updated
collection['meanlist'].hist(density=True, bins=100, figsize=(15,8))
plt.show()
#Sampling from arbritary distribution
#See what central limit theorem tells you...the sample size is larger enough,
#the distribution of sample mean is approximately normal
#apop is not normal, but try to chnage the sample size from 100 to a larger number
#The distribution of sample mean of apop becomes normal
sample_size = 100
samplemeanlist = []
apop = pd.DataFrame([1, 0, 1, 0, 1])
for t in range(10000):
    sample = apop[0].sample(sample_size, replace=True) #small sample size
    samplemeanlist.append(sample.mean())
accollec = pd.DataFrame()
accollec['meanlist'] = samplemeanlist
accollec.hist(density=True, bins=100, figsize=(15,8))
plt.show()