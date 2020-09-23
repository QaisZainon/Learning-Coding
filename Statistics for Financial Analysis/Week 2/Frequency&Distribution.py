import pandas as pd 
import matplotlib.pyplot as plt 
#To recall, this is the code to mimic the roll dice game for 50 times
die = pd.DataFrame([1,2,3,4,5,6])
trial = 50
results = [die.sample(2, replace = True).sum().loc[0] for i in range(trial)]
#This is the code for summarizing the results of sum of faces by frequency
freq = pd.DataFrame(results)[0].value_counts() #makes it into a line
sort_freq = freq.sort_index()
print(sort_freq)
#plot the bar chart base on the result
plt.title('50 Rolls')
plt.xlabel('Dice Rolls')
plt.ylabel('Roll Amount')
sort_freq.plot(kind='bar', color='blue', figsize=(15, 8))
plt.show()
#Using relative frequency, we can rescale the frequency so that 
#we can compare results from different number of trials
relative_freq = sort_freq/trial
plt.title('50 Rolls')
plt.xlabel('Dice Rolls')
plt.ylabel('Roll Frequency')
sort_freq.plot(kind='bar', color='blue', figsize=(15, 8))
plt.show()
#Let us try to increase the number of trials to 10000, and see what will happen...
trial = 10000
results = [die.sample(2, replace=True).sum().loc[0] for i in range(trial)]
freq = pd.DataFrame(results)[0].value_counts()
sort_freq = freq.sort_index()
relative_freq = sort_freq/trial
plt.title('10000 Rolls')
plt.xlabel('Dice Rolls')
plt.ylabel('Roll Frequency')
relative_freq.plot(kind='bar', color='blue', figsize=(15, 8))
plt.show()

