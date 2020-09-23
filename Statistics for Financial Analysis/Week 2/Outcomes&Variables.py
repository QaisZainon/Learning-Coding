#import numpy and pandas package
import numpy as np 
import pandas as pd 
#roll two dice for multiple times
die = pd.DataFrame([1,2,3,4,5,6])
sum_of_dice = die.sample(2, replace = True).sum().loc[0] #the .loc is there because the DataFrame is a table
print('Sum of dice is', sum_of_dice)
#The following code mimics the roll dice game for 50 times. And the results are all stored into 'Result'
#Lets try and get the results of 50 sum of faces
trial = 50
result = [die.sample(2, replace=True).sum().loc[0] for i in range(trial)]
#print the first 10 results
print(result[:10])