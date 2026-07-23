import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset('titanic')

print(data.shape)
print(data.dtypes)
print(data.describe())
print(data.head(10))
print(data.tail(10))
print(data['class'].unique())
print(data.columns.to_list())
print(data.value_counts())


# plots
data['age'].plot(kind = 'hist', bins = 30, edgecolor = 'black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.show()