import numpy as np
import pandas as pd

def load_data():
    df=pd.read_excel("商品订单.xlsx")
    data = df.values[:,[2]]
    data_set=[]
    for i in range(len(data)):
        data_set.append(str(data[i])[2:len(str(data[i]))-2].split('，'))
    return data_set
