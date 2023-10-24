import warnings
warnings.filterwarnings("ignore")

import pandas as pd

# Загрузка данных
data = pd.read_csv('C:/Users/lucky/Documents/University/7s semestr/big data/github/big-data/Auto_dataset.csv')

# Находим компанию с самой высокой и низкой ценой
most_expensive = data.loc[data['price'].idxmax()]['company']
least_expensive = data.loc[data['price'].idxmin()]['company']

print(f'Most Expensive: {most_expensive}')
print(f'Least Expensive: {least_expensive}')