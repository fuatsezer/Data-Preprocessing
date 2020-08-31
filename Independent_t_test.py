#%% Indipendent t test - binary categoric-continious
from scipy import stats
class1_score = np.array([45.0, 40.0, 49.0, 52.0, 54.0, 64.0,
                    36.0, 41.0, 42.0, 34.0])
class2_score = np.array([75.0, 85.0, 53.0, 70.0, 72.0, 93.0,
                    61.0, 65.0, 65.0, 72.0])
print(stats.ttest_ind(class1_score,class2_score))

