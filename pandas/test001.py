import numpy as np
import pandas as pd

df=pd.read_excel("商品订单.xlsx")
data = df.values[:,[0,2]]
print(data[1])


