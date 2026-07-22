import pandas as pd
import numpy as np
import seaborn as sns

data = sns.load_dataset('titanic')

data['age'] = data['age'].fillna(data['age'].median())

#children, rich_women, first_or_second
children = data[data['age'] < 18]
print('children', len(children))

rich_women = data[(data['sex'] == 'female') & (data['pclass'] == 1)]
print('rich women 1st class', len(rich_women))

first_or_second = data[(data['pclass'] == 1) | (data['pclass'] == 2)]
print('first or second class', len(first_or_second))

