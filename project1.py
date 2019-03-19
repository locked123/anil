# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 22:37:04 2019

@author: bir bdr thapa
"""
"""
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style 
import pandas as pd
import pandas_datareader.data as web

style.use('ggplo`;t')
start=dt.datetime(2000,1,1)
end=dt.datetime(2016,12,31)

df=web.DataReader('TSLA','yahoo',start,end)
print(df.head())
"""


import pandas_datareader.data as web
import datetime as dt
start=dt.datetime(2000,1,1)
end=dt.datetime(20180,12,31)
stock='^DJI'
df=web.DataReader(stock,'yahoo',start,end)
print(df.head())