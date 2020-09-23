import pandas as pd 
import numpy as np 
#Create a Population DataFrame with 10 data
data = pd.DataFrame()
data['Population'] = [47, 48, 85, 20, 19, 13, 72, 16, 50, 60]
#Draw sample with replacement, size=5 from Population
a_sample_with_replacement = data['Population'].sample(5, replace=True)
print(a_sample_with_replacement)
a_sample_without_replacement = data['Population'].sample(5, replace=False)
print(a_sample_without_replacement)
#Calculate mean and variance
population_mean = data['Population'].mean()
population_var = data['Population'].var(ddof=0)
print('Population mean is', population_mean)
print('Population variance is', population_var)
#Calculate sample mean and sample standard deviation, size=10
#You will get different mean and variance every time when yuo execute the below code
a_sample = data['Population'].sample(10, replace=True)
sample_mean = a_sample.mean()
sample_var = a_sample.var()
print('Sample mean is ', sample_mean)
print('Sample variance is ', sample_var)
#Average of an unbiased estimator
sample_length = 500
sample_variance_collection =[data['Population'].sample(10, replace=True).var(ddof=1) for i in range(sample_length)]
print(sample_variance_collection)