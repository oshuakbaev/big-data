import warnings
warnings.filterwarnings("ignore")

import pandas as pd

# Загрузка данных
data = pd.read_csv('C:/Users/lucky/Documents/University/7s semestr/big data/github/big-data/Auto_dataset.csv')
df1 = pd.read_csv(data)


merged_data = pd.concat([df1,df2['Mileage']],axis=1)
print(merged_data)