# -*- coding: utf-8 -*-

import os
import pandas as pd
import numpy as np

#path = os.path.dirname(os.path.abspath(__file__))

#exc = os.path.join(path,"test008")

#固定盘
exc = "/Users/focus/Desktop/test008"
#新建列表，存放文件名（可以忽略，但是为了做的过程能心里有数，先放上）
filename_excel = []

#新建列表，存放每个文件数据框（每一个excel读取后存放在数据框）
frames = []

for root, dirs, files in os.walk(exc):
    for file in files:
        if os.path.splitext(file)[1] == '.xlsx':
            print(os.path.join(root,file))
            filename_excel.append(os.path.join(root,file))
            df = pd.read_excel(os.path.join(root,file)) #excel转换成DataFrame
            frames.append(df)
#打印文件名
print(filename_excel)   
 #合并所有数据
result = pd.concat(frames,sort=False)    

#查看合并后的数据
result.head()
result.shape

#保存为csv
#save = os.path.join(exc,"0001.csv")
#result.to_csv(save,sep=',',index = False,encoding="utf-8_sig")

#保存为excel
writer = os.path.join(exc,"0001.xlsx")
result.to_excel(writer, '数据源',index=False,float_format='%.8f')
