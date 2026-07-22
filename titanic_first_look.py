import pandas as pd
import numpy as np
import seaborn as sns

data = sns.load_dataset('titanic')

print(data.shape)
print(data.dtypes)
print(data.describe())
print(data.head(10))
print(data.tail(10))
print(data['class'].unique())
print(data.columns.to_list())
print(data.value_counts())