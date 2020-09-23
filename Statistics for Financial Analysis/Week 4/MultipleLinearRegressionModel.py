import pandas as pd 
import statsmodels.api as smf
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# Import all stock market data into DataFrame
aord   = pd.read_csv(r'C:\Users\Dr. Wan Asna\Desktop\Python Projects\Statistics for Financial Analysis\Week 4\Stock_csv\^AORD.csv')
nikkei = pd.read_csv(r'C:\Users\Dr. Wan Asna\Desktop\Python Projects\Statistics for Financial Analysis\Week 4\Stock_csv\^N225.csv')
hsi    = pd.read_csv(r'C:\Users\Dr. Wan Asna\Desktop\Python Projects\Statistics for Financial Analysis\Week 4\Stock_csv\^HSI.csv')
daxi   = pd.read_csv(r'C:\Users\Dr. Wan Asna\Desktop\Python Projects\Statistics for Financial Analysis\Week 4\Stock_csv\^GDAXI.csv')
cac40  = pd.read_csv(r'C:\Users\Dr. Wan Asna\Desktop\Python Projects\Statistics for Financial Analysis\Week 4\Stock_csv\^FCHI.csv')
sp500  = pd.read_csv(r'C:\Users\Dr. Wan Asna\Desktop\Python Projects\Statistics for Financial Analysis\Week 4\Stock_csv\^GSPC.csv')
dji    = pd.read_csv(r'C:\Users\Dr. Wan Asna\Desktop\Python Projects\Statistics for Financial Analysis\Week 4\Stock_csv\^DJI.csv')
nasdaq = pd.read_csv(r'C:\Users\Dr. Wan Asna\Desktop\Python Projects\Statistics for Financial Analysis\Week 4\Stock_csv\^IXIC.csv')
spy    = pd.read_csv(r'C:\Users\Dr. Wan Asna\Desktop\Python Projects\Statistics for Financial Analysis\Week 4\Stock_csv\SPY.csv')

# Step 1 : Data Munging
# Timezone issues, extract and calculate appropriate stock market data for analysis
# Indicepanel is the DataFrame of our training model
indicepanel = pd.DataFrame(index = spy.index)

indicepanel['spy']      = spy['Open'].shift(-1) - spy['Open']
indicepanel['spy_lag1'] = indicepanel['spy'].shift(1)
indicepanel['sp500']    = sp500['Open'] - sp500['Open'].shift(1)
indicepanel['nasdaq']   = nasdaq['Open'] - nasdaq['Open'].shift(1)
indicepanel['dji']      = dji['Open'] - dji['Open'].shift(1)

indicepanel['cac40']    = cac40['Open'] - cac40['Open'].shift(1)
indicepanel['daxi']     = daxi['Open'] - daxi['Open'].shift(1)

indicepanel['aord']     = aord['Close'] - aord['Open']
indicepanel['hsi']      = hsi['Close'] - hsi['Open']
indicepanel['nikkei']   = nikkei['Close'] - nikkei['Open']
indicepanel['Price']    = spy['Open']

print(indicepanel.head())
# Checking NaN value in indicepanel
print(indicepanel.isnull().sum())
# Save
path_save = r'C:\Users\Dr. Wan Asna\Desktop\Python Projects\Statistics for Financial Analysis\Week 4\indicepanel.csv'
indicepanel.to_csv(path_save)
print(indicepanel.shape)

# Step 2 : Data Splitting
Train = indicepanel.iloc[-1000:, :]
Test = indicepanel.iloc[0:1000, :]
print(Train.shape, Test.shape)

# Step 3 : Explore the train data set
from pandas.plotting import scatter_matrix
sm = scatter_matrix(Train, figsize=(10, 10))
plt.show()

# Step 4 : Check the correlation of each index between spy
# Find the indice with largest correlation
corr_array = Train.iloc[:, :-1].corr()['spy']
print(corr_array)
formula = 'spy~spy_lag1 + sp500 + nasdaq + dji + cac40 + aord + daxi + nikkei + hsi'
lm = smf.OLS.from_formula(formula, Train).fit()
lm.summary()

# Step 5 : Make prediction
Train['PredictedY'] = lm.predict(Train)
Test['PredictedY'] = lm.predict(Test)
plt.scatter(Train['spy'], Train['PredictedY'])

# Step 6 : Model evaluation - Statistical standard
# RMSE - Root Mean Squared Error, Adjusted R^2
def adjustedMetric(data, model, model_k, yname):
    data['yhat'] = model.predict(data)
    SST = ((data[yname] - data[yname].mean())**2).sum()
    SSR = ((data['yhat'] - data[yname].mean())**2).sum()
    SSE = ((data[yname] - data['yhat'])**2).sum()
    r2 = SSR/SST
    adjustR2 = 1 - (1 - r2)*(data.shape[0] - 1)/(data.shape[0] - model_k -1)
    RMSE = (SSE/(data.shape[0] - model_k -1))**0.5
    return adjustR2, RMSE
def assessTable(test, train, model, model_k, yname):
    r2test, RMSEtest = adjustedMetric(test, model, model_k, yname)
    r2train, RMSEtrain = adjustedMetric(train, model, model_k, yname)
    assessment = pd.DataFrame(index=['R2', 'RMSE'], columns=['Train', 'Test'])
    assessment['Train'] = [r2train, RMSEtrain]
    assessment['Test'] = [r2test, RMSEtest]
    return assessment
# Get the assement table for our model
print(assessTable(Test, Train, lm, 9, 'spy'))
# AHHHHHH I HAVE NO CLUE WHAT IS GOING ON AAAAAAAAH