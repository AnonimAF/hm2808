# Задача 44: В ячейке ниже представлен код генерирующий DataFrame,
# которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид.
# Сможете ли вы это сделать без get_dummies?

import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()


data1 = pd.DataFrame({'whoAmI_human':data['whoAmI'].apply(lambda x: 1 if x == 'human' else 0)})
whoAmI_robot = pd.DataFrame({'whoAmI_robot':data['whoAmI'].apply(lambda x: 1 if x == 'robot' else 0)})
data1['whoAmI_robot'] = whoAmI_robot

print(data1)