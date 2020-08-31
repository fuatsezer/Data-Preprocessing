#%% DBSCAN
import pandas as pd
from pylab import rcParams
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn
from sklearn.cluster import DBSCAN
from collections import Counter
from sklearn.neighbors import NearestNeighbors
rcParams["figure.figsize"] = 5,4
df=pd.read_csv("titanic.csv")
X = df.drop(["Survived","Name","Sex","Ticket","Cabin","Embarked","Age"],axis=1)
y=df.Survived
#%% choosing epsilon
neigh = NearestNeighbors(n_neighbors=2)
nbrs = neigh.fit(X)
distances, indices = nbrs.kneighbors(X)
distances = np.sort(distances, axis=0)
distances = distances[:,1]
plt.plot(distances)

#%%
model = DBSCAN(eps = 32,min_samples=3).fit(X)
print(model)
#%%
outliers_df=pd.DataFrame(X)
print(Counter(model.labels_))
print(outliers_df[model.labels_ == -1 ])
#%%
fig = plt.figure()
ax = fig.add_axes([.1,.1,1,1])
colors = model.labels_
ax.scatter(X.Fare,X.SibSp,c=colors)
#%% Local Outlier Factor
from sklearn.neighbors import LocalOutlierFactor
clf = LocalOutlierFactor(n_neighbors=2)
clf.fit_predict(X)
score=clf.negative_outlier_factor_
print(len(score[score<-2]))


