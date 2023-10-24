import warnings
warnings.filterwarnings("ignore")

import pandas as pd

# Загрузка данных
data = pd.read_csv('C:/Users/lucky/Documents/University/7s semestr/big data/github/big-data/Auto_dataset.csv')

expensive_car_per_company = data.loc[data.groupby('company')['price'].idxmax()]
print(expensive_car_per_company)