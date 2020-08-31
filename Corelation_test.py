import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
#%% Normality test
# zero hypotesis is normal
mpg = [21.0, 21.0, 22.8, 21.4, 18.7, 18.1, 14.3, 24.4, 22.8,
       19.2, 17.8, 16.4, 17.3, 15.2, 10.4, 10.4, 14.7, 32.4, 30.4,
       33.9, 21.5, 15.5, 15.2, 13.3, 19.2, 27.3, 26.0, 30.4, 15.8,
       19.7, 15.0, 21.4]
hp = [110, 110, 93, 110, 175, 105, 245, 62, 95, 123, 123, 180,
      180, 180, 205, 215, 230, 66, 52, 65, 97, 150, 150, 245,
      175, 66, 91, 113, 264, 175, 335, 109]
print(stats.shapiro(mpg))
print(stats.shapiro(hp))
plt.hist(hp)
#%% parametric pearson test
print(stats.pearsonr(mpg,hp))
#%% spearman spearman test
print(stats.spearmanr(mpg,hp))




