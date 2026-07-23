import seaborn as sns
import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt

data = sns.load_dataset('titanic')

missing_count = data.isna().sum()
missing_count_pct = (data.isna().sum() / len(data)) * 100

missing_count_data = pd.DataFrame({
    'missing count' : missing_count,
    'missing count pct' : missing_count_pct
})

print(missing_count_data)


#fill the age with medians
data['age'] = data['age'].fillna(data['age'].median())

#remove the deck cus its almost empty and not needed
data = data.drop(columns = ['deck'])

data['embarked'] = data['embarked'].fillna(data['embarked'].mode()[0])
data['embark_town'] = data['embark_town'].fillna(data['embark_town'].mode()[0])

#check to see if the data is cleaned now
print('cleaned data', data.isna().sum())

missing_count.plot(kind = 'bar', color = 'salmon')
plt.title('Missing Values by Column')
plt.ylabel('Count')
plt.show()