import seaborn as sns
import pandas as pd

data = sns.load_dataset('titanic')
data['age'] = data['age'].fillna(data['age'].median())

# New column from arithmetic
data['family_size'] = data['sibsp'] + data['parch'] + 1

# Custom function + apply
def family_type(size):
    if size == 1:
        return 'Solo'
    elif size <= 4:
        return 'Small'
    else:
        return 'Large'

data['family_type'] = data['family_size'].apply(family_type)

# Sort by one column
print(data.sort_values('fare', ascending=False).head())

# Sort by multiple columns
print(data.sort_values(['pclass', 'age'], ascending=[True, False]).head())

# Pivot table-pd.pivot_table(var_name, index(rows), columns, values(what to calc, which func to perform))
pivot = pd.pivot_table(data, index='pclass', columns='sex', values='survived', aggfunc='mean')
print(pivot)
# Export what you built
data.to_csv('titanic_final.csv', index=False)
pivot.to_excel('titanic_pivot.xlsx', sheet_name='Pivot')