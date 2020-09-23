import pandas as pd 
import matplotlib.pyplot as plt 
#assume that we have fair dice, which means all faces will be shown with equal probability
#then we can say we know the 'Distribution' of the random variable - sum_of_dice
X_distri = pd.DataFrame(index=[2,3,4,5,6,7,8,9,10,11,12])
X_distri['Prob'] = [1,2,3,4,5,6,5,4,3,2,1]
X_distri['Prob'] = X_distri['Prob']/36
mean = pd.Series(X_distri.index * X_distri['Prob']).sum()
var = pd.Series(((X_distri.index - mean)**2)*X_distri['Prob']).sum()
#Output the mean and variance of the distribution. Mean and variance can be used to describe a distribution
print(mean, var)
#If we calculate mean and variance of outcomes (with high enough number of trials, eg 20000)...
trial = 20000
die = pd.DataFrame([1,2,3,4,5,6])
results = [die.sample(2, replace=True).sum().loc[0] for i in range(trial)]
results = pd.Series(results)
print(results.mean(), results.var())
