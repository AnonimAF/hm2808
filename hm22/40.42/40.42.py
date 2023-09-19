# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке sample_data.
# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).
import pandas as pd

data = pd.read_csv('california_housing_train.csv')

print(data[(data['population'] >= 0) & (data['population'] <= 500)]['median_house_value'].mean())