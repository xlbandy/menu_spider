import pandas as pd
import numpy as np
df = pd.read_csv('foods.csv', encoding='utf8')

#df.info()

#print(df.describe())

#print(df.columns)

#print(tabulate(df,headers = df.columns))

print(df.head(5))