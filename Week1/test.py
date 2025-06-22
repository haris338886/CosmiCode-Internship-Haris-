import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.DataFrame({
    'x': np.arange(1, 11),
    'y': np.random.randint(10, 100, size=10)
})
sns.barplot(x='x', y='y', data=data)
plt.title("Sample Bar Plot")
plt.show()
