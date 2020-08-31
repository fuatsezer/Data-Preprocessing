from sklearn.impute import KNNImputer
import pandas as pd
print(df.isna().sum())
imputer = KNNImputer()
X=df[["Survived","Pclass","SibSp","Age"]]
X = imputer.fit_transform(X)
print(pd.DataFrame(X).isna().sum())


