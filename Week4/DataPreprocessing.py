from sklearn.datasets import load_iris
import pandas as pd
import numpy as np

iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target

print("First 5 rows of dataset:")
print(df.head())

print("\nMissing values before simulation:")
print(df.isnull().sum())

df.loc[0, 'sepal length (cm)'] = np.nan
print("\nMissing values after introducing NaN:")
print(df.isnull().sum())
df['sepal length (cm)'].fillna(df['sepal length (cm)'].mean(), inplace=True)
print("\nMissing values after filling with mean:")
print(df.isnull().sum())
print("\nFinal dataset preview after preprocessing:")
print(df.head())
