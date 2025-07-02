import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression

iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target

df.fillna(df.mean(), inplace=True)

X = df[['sepal length (cm)']]  # Independent variable
y = df['petal length (cm)']    # Dependent variable

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

plt.figure(figsize=(8,6))
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, y_pred, color='red', linewidth=2, label='Regression Line')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.title('Linear Regression: Sepal Length vs Petal Length')
plt.legend()
plt.grid(True)
plt.show()

print(f"Model Coefficient (Slope): {model.coef_[0]:.4f}")
print(f"Model Intercept: {model.intercept_:.4f}")
