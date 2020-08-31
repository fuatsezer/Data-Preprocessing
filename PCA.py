import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#% temel bileşen sayısına karar verme
cor=df.corr()
eigen=np.linalg.eig(cor)

prop_var = eigen[0] / eigen[0].sum()

cum_prop_var = np.cumsum(prop_var)
print(cum_prop_var)
plt.plot(prop_var)
#%% PCA uygulama
from sklearn.decomposition import PCA
pca = PCA(n_components=6)
X = pca.fit_transform(X)
