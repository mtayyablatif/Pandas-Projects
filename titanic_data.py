import seaborn as sns
import pandas as pd
import numpy as np

data = sns.load_dataset('titanic')

# print(data)
# print(data.head(20))
# print(data.shape)
# print(data.info())
# print(data.describe())

print(data.isna().sum())  # finds the number of missing elements

# cleaning the data, removing deck and adding median age in missing age
data['age'] = data['age'].fillna(data['age'].median())
data = data.drop(columns=['deck'])

# sanity check - age should now show 0 missing
print(data.isna().sum())

children = data[data['age'] < 18]
print("Child survival rate:", children['survived'].mean())

print(data.groupby(['sex', 'class'])['survived'].mean())
print(data.groupby(['embarked'])['survived'].count())

print(data['pclass'].value_counts())
print(data['embark_town'].value_counts())

print(data.sort_values('age', ascending=False).head())
print(data.sort_values('age').head())

# New column
data['family_size'] = data['sibsp'] + data['parch'] + 1

# Apply custom function
def family_type(size):
    if size == 1:
        return 'Solo'
    elif size <= 4:
        return 'Small'
    else:
        return 'Large'

data['family_type'] = data['family_size'].apply(family_type)
print(data['family_type'].value_counts())

# Pivot table
pivot1 = pd.pivot_table(data, index='pclass', columns='sex', values='survived', aggfunc='mean')
print(pivot1)

data.to_excel('titanic_cleaned.xlsx', index=False, sheet_name='Titanic')
pivot1.to_excel('titanic_pivot.xlsx', sheet_name='Pivot')