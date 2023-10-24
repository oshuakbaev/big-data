import warnings
warnings.filterwarnings("ignore")

import pandas as pd

# Загрузка данных
data = pd.read_csv('C:/Users/lucky/Documents/University/7s semestr/big data/github/big-data/Auto_dataset.csv')

bmw_data = data[data['company'] == 'bmw']
print(bmw_data)