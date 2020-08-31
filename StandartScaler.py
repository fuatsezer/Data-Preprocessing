#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("titanic.csv")
#%% Decision 
print(df.describe())
#%% Değişkenlerin ortalaması birbirinden çok farklı ise scale uygulayın
X=df[["Pclass","SibSp","Parch","Fare"]]
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X=scaler.fit_transform(X)
