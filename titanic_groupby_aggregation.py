import numpy as np
import pandas as pd
import seaborn as sns

data = sns.load_dataset('titanic')
data['age'] = data['age'].fillna(data['age'].median())

# data_var_name.groupby('required_column')[what_we_need].func_we_need_to_perform()
print(data.groupby('sex')['survived'].mean())

#multiple categories grouped
print(data.groupby(['sex', 'pclass'])['survived'].mean())

print(data.groupby('pclass')['age'].agg(['min', 'max', 'mean', 'count']))

print(data.groupby('pclass')['age'].max())

print(data['pclass'].value_counts())

# .size() counts ALL rows in a group (including NaN)
# .count() counts only NON-NULL values in a specific column
print(data.groupby('pclass').size())          # counts rows
print(data.groupby('pclass')['age'].count())  # counts non-null ages


# reset_index() turns groupby result back into a flat DataFrame
survival_by_class = data.groupby('pclass')['survived'].mean().reset_index()
print(survival_by_class)

