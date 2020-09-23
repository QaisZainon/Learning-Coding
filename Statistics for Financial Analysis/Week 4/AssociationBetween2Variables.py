import pandas as pd 
import matplotlib.pyplot as plt 
#Import the housing information for analysis
Consumption = pd.read_csv(
    'C:\\Users\\Dr. Wan Asna\\Desktop\\Python Projects\\Statistics for Financial Analysis\\Week 4\\TourismConsumption.csv', 
    encoding = 'unicode_escape', index_col= 0
    )
print(Consumption)
#Use covariance to calculate the association
Consumption.cov()
#Use correlation to calculate the association
Consumption.corr()
#Scatter matrix plot
pd.plotting.scatter_matrix(Consumption, figsize = (10, 10))
plt.show()
#This time we'll take a close look at Travel vs Fuel. What is the association
Consumption.plot(kind = 'scatter', x ='Travel', y='Fuel', figsize=(10,10))
plt.show()