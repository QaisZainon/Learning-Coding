import pandas as pd 
import statsmodels.api as sm
import matplotlib.pyplot as plt 
housing = pd.read_csv(r'C:\Users\Dr. Wan Asna\Desktop\Python Projects\Statistics for Financial Analysis\Week 4\Boston.csv')
print(housing.head())
model = sm.OLS.from_formula('medv~lstat', housing).fit()
#Estimated intercept and slope by least square estimation
b0_ols = model.params[0]
b1_ols = model.params[1]
housing['BestResponse'] = b0_ols + b1_ols*housing['lstat']
'''Linearity'''
#Checking scatter plot
housing.plot(kind='scatter', x='lstat', y='medv', figsize=(10,10), color='g')
plt.show()
'''Independence'''
#Get all errors(residuals)
housing['error'] = housing['medv'] - housing['BestResponse']
#Error vs order plot (residual vs order) as a fast check
plt.figure(figsize=(15, 8))
plt.title('Residual vs order')
plt.plot(housing.index, housing['error'], color='purple')
plt.axhline(y=0, color='red')
plt.show()
'''Normality'''
import scipy.stats as stats
z = (housing['error'] - housing['error'].mean())/housing['error'].std(ddof=1)
stats.probplot(z, dist='norm', plot=plt)
plt.title('Normal Q-Q plot')
plt.show()
'''Equal Variance'''
#Residual vs predictor plot
housing.plot(kind='scatter', x='lsts', y='error', figsize=(15, 8), color='green')
plt.title('Residual vs predictor')
plt.axhline(y=1, color='red')
plt.show()
