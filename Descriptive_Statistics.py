import pandas as pd
df = pd.read_csv("titanic.csv")
#%% Frequency table for categorical variables
freq_table_survived= df["Survived"].value_counts(normalize=True)
count_table_survived= df["Survived"].value_counts()
#%% Frequency table for discrete variables
freq_table_pclass= df["Pclass"].value_counts(normalize=True)
#%% Frequency table for continious variables
freq_table_fare= pd.cut(df["Fare"],[0,50,100,150,200,250]).value_counts(normalize=True)
#%% pie chart
import matplotlib.pyplot as plt
plt.pie(freq_table_survived,labels=freq_table_survived.index,autopct='%1.1f%%',shadow=True)
plt.show()
#%% Pareto chart
from matplotlib.ticker import PercentFormatter
df["cumpercentage"] = count_table_survived.cumsum()/count_table_survived.sum()*100
fig, ax = plt.subplots()
ax.bar(count_table_survived.index, count_table_survived, color="C0")
ax2 = ax.twinx()
ax2.plot(df.index, df["cumpercentage"], color="C1", marker="D", ms=7)
ax2.yaxis.set_major_formatter(PercentFormatter())

ax.tick_params(axis="y", colors="C0")
ax2.tick_params(axis="y", colors="C1")
plt.show()
#%% 
#If Sk1 1⁄4 0, the distribution is symmetrical;
# If Sk1 > 0, the distribution is positively skewed (to the right); 
# If Sk1 < 0, the distribution is negatively skewed (to the left).
# If k = 0.263, we say that the curve is mesokurtic;
# If k > 0.263, we say that the curve is platykurtic; 
# If k < 0.263, we say that the curve is leptokurtic.
from scipy import stats
def describe(df):
    return pd.concat([df.describe().T,
                      df.median().rename('median'),
                      df.mad().rename('mad'),
                      df.skew().rename('skew'),
                      df.kurt().rename('kurt'),
                      df.sem().rename("SE")
                     ], axis=1).T
desc= describe(df)
#%% Standart hata, ortalamanın standart sapmasıdır. 
#Standart sapmayı popülasyonun kareköküne veya örneklem büyüklüğüne bölerek elde edilir



