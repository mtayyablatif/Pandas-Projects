import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

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

# Pivot table
pivot = pd.pivot_table(data, index='pclass', columns='sex', values='survived', aggfunc='mean')
print(pivot)

data.to_csv('titanic_final.csv', index=False)
pivot.to_excel('titanic_pivot.xlsx', sheet_name='Pivot')



# Survival rate by class and sex
pivot.plot(kind='bar')
plt.title('Survival Rate by Class and Sex')
plt.ylabel('Survival Rate')
plt.savefig('survival_by_class_sex.png')   # save BEFORE show
plt.show()

# Family type distribution
data['family_type'].value_counts().plot(kind='bar', color='teal')
plt.title('Family Size Category Distribution')
plt.ylabel('Count')
plt.savefig('family_type_distribution.png')   # save BEFORE show
plt.show()