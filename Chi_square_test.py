#%% The chi-square test of independence- categoric-categoric
from scipy import stats
# cross = pd.crosstab(df["native.country"],df["income"])
men_women = np.array([[100, 120, 60],[350, 200, 90]])
print(stats.chi2_contingency(men_women))

