import warnings
warnings.filterwarnings("ignore")

import pandas as pd

# Загрузка данных
data = pd.read_csv('C:/Users/lucky/Documents/University/7s semestr/big data/github/big-data/Auto_dataset.csv')

# Замена ? и n.a на NaN
data.replace(['?', 'n.a'], pd.NA, inplace=True)

# Заполнение пропущенных значений (NaN)
data.fillna(method ='ffill', inplace = True)

# Сохранение обновленного файла
data.to_csv('C:/Users/lucky/Documents/University/7s semestr/big data/github/big-data/Auto_dataset.csv', index=False)
