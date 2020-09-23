import pandas as pd 
import statsmodels.api as smf 
import matplotlib.pyplot as plt 
housing = pd.read_csv(r'C:\Users\Dr. Wan Asna\Desktop\Python Projects\Statistics for Financial Analysis\Week 4\Boston.csv')
print(housing.head())
#Guessing the real values of intercept and slope
#We call our guess b0, b1...
#Try to assign the value of b0, b1 to get a straight line that can describe our data
b0 = 0.1
b1 = 1
housing['GuessResponse'] = b0 + b1*housing['rm']
#Least square estimates
#Input the formula (lecture video 4.3)
formula = 'medv~rm'
model = smf.OLS.from_formula(formula, housing).fit() #the course was outdated
#Estimated intercept and slope by least square estimation
#Attribute 'params' returns a list of estimated form model
b0_ols = model.params[0]
b1_ols = model.params[1]
housing['BestResponse'] = b0_ols + b1_ols*housing['rm']
#Checking for the error of guess...
housing['error'] = housing['medv'] - housing['BestResponse']
#This shows how far the guess response is from the true response
housing['observederror'] = housing['medv'] - housing['GuessResponse']
#plot the estimated line together with the points
plt.figure(figsize=(10,10))
plt.title('Sum of squared error is {}'.format(((housing['observederror'])**2).sum()))
plt.scatter(housing['rm'], housing['medv'], color='g', label='Observed')
plt.plot(housing['rm'], housing['GuessResponse'], color='red', label='GuessResponse')
plt.plot(housing['rm'], housing['BestResponse'], color='yellow', label='BestResponse')
plt.legend()
plt.xlim(housing['rm'].min()-2, housing['rm'].max()+2)
plt.ylim(housing['medv'].min()-2, housing['medv'].max()+2)
plt.show()
#Refer to the P-value of RM, Confidence Interval and R-square to evaluate the performance
model.summary()
