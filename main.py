import os 
import sys 
import pandas as pd 
import numpy as np 

df = pd.read_csv('data.csv')

df.head()

df.columns()

data = pd.to_excel('cleaned_data.xlsx', index=False)
data.describe()
data.info()
print("Data processing complete.").tolist()