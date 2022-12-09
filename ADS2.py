# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 11:44:28 2022

@author: aishw
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy as sc

#defining the function for loading filename as argument
def loadfile(filename):
   df_x = pd.read_csv(filename,skiprows = 3)
   df_x = df_x.iloc[[4,14,21,37],[0,52,53,54,55]]
   df_x = df_x.reset_index(drop=True)
   df_y = df_x.T
   print(df_x)
   print(df_y)
   return df_x, df_y

df1, df11 = loadfile('Total green house gas emissions.csv')

df1.plot()
df1.plot(kind='bar')
