import pandas as pd

columns = [f'feature_{i}' for i in range(57)] + ['spam']  # Last column is target: 1 = spam, 0 = not spam

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/spambase/spambase.data"
df = pd.read_csv(url, header=None, names=columns)

print(df.head())
