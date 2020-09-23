import statsmodels.api as smf 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import warnings
warnings.filterwarnings('ignore')
indicepanel = pd.read_csv(r'C:\Users\Dr. Wan Asna\Desktop\Coding Projects\Statistics for Financial Analysis\Week 4\indicepanel.csv')
print(indicepanel.head())
Train = indicepanel.iloc[-1000: , : ]
formula = 'spy~spy_lag1 + sp500 + nasdaq + dji + cac40 + aord + daxi + nikkei + hsi'
lm = smf.OLS.from_formula(formula, Train).fit()
Train['PredictedY'] = lm.predict(Train)
#Profit of Signal-based startergy
Train['Order'] = [1 if sig>0 else -1 for sig in Train['PredictedY']]
Train['Profit'] = Train['spy'] * Train['Order']
Train['Wealth'] = Train['Profit'].cumsum()
print('Total profit made in Train: ', Train['Profit'].sum())
plt.figure(figsize=(10,10))
plt.title('Performance of Strategy in Train')
plt.plot(Train['Wealth'].values, color='green', label='Sigma based startegy')
plt.plot(Train['spy'].cumsum().values, color='red', label='Buy and Hold strategy')
plt.legend()
plt.show()
Train['Wealth'] = Train['Wealth'] + Train.loc[Train.index[0], 'Price']
# Sharpe Ratio on Train data
Train['Return'] = np.log(Train['Wealth']) - np.log(Train['Wealth'].shift(1))
dailyr = Train['Return'].dropna()
print('Daily Sharpe Ratio is ', dailyr.mean()/dailyr.std(ddof=1))
print('yearly Sharpe Ratio is ', (252**0.5)*dailyr.mean()/dailyr.std(ddof=1))
# Maximum Drawdown in Train data
Train['Peak'] = Train['Wealth'].cummax()
Train['Drawdown'] = (Train['Peak'] - Train['Wealth'])/Train['Peak']
print('Maximum Drawdown in Train is ', Train['Drawdown'].max())