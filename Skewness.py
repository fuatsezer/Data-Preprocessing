import numpy as np
import matplotlib.pyplot as plt
#%%
X = np.random.uniform(0,100,1000)
X =X.reshape((500,2))
plt.hist(X)
#%% test skewness
from scipy import stats
# skewness = 0 : normally distributed.
# skewness > 0 : more weight in the left tail of the distribution.
# skewness < 0 : more weight in the right tail of the distribution. 
print(stats.skew(X))
#%%
stats.probplot(X[:,0], dist="norm", plot=plt)
#%% normalize the feature
from sklearn.preprocessing import  Normalizer
normalizer = Normalizer(norm="l2").fit(X)
X = normalizer.transform(X)
plt.hist(X)
plt.show()
#%%
print(stats.skew(X))
#%%
stats.probplot(X[:,1], dist="norm", plot=plt)


