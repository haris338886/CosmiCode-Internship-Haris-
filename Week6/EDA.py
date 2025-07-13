import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/spambase/spambase.data"
columns = [f'feature_{i}' for i in range(57)] + ['spam']
df = pd.read_csv(url, header=None, names=columns)

print("Missing values per column:\n", df.isnull().sum())
print("\nData types:\n", df.dtypes)
print("\nDuplicate rows:", df.duplicated().sum())

scaler = StandardScaler()
X_scaled = scaler.fit_transform(df.drop('spam', axis=1))

plt.figure(figsize=(6,4))
sns.countplot(x='spam', data=df)
plt.title("Spam vs Non-Spam Count")
plt.xticks([0, 1], ['Not Spam (0)', 'Spam (1)'])
plt.xlabel("Email Type")
plt.ylabel("Count")
plt.show()

print("\nClass distribution:\n", df['spam'].value_counts(normalize=True))
print("\nSummary statistics:\n", df.describe())

plt.figure(figsize=(12, 10))
correlation = df.corr()
sns.heatmap(correlation, cmap="coolwarm", square=True, cbar_kws={'shrink': .5}, vmax=1.0, vmin=-1.0)
plt.title("Feature Correlation Heatmap")
plt.show()

spam_corr = correlation['spam'].drop('spam').sort_values(key=np.abs, ascending=False).head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=spam_corr.index, y=spam_corr.values)
plt.title("Top 10 Features Correlated with Spam")
plt.xticks(rotation=45)
plt.ylabel("Correlation with Spam")
plt.show()

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
plt.figure(figsize=(8,6))
sns.scatterplot(x=X_pca[:,0], y=X_pca[:,1], hue=df['spam'], palette=['blue','red'], alpha=0.6)
plt.title("PCA Projection of Emails")
plt.xlabel("PCA 1")
plt.ylabel("PCA 2")
plt.legend(title='Spam')
plt.show()
