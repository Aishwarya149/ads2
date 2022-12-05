# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 11:44:28 2022

@author: aishw
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy as sc

df_ads2 = pd.read_csv("ads2.csv")
print(df_ads2)
print()
print(df_ads2.describe())

df_ads2_t = pd.DataFrame.transpose(df_ads2)
print(df_ads2_t)

# total rows and columns
#df_ads2.shape

df_ads2.drop(df_ads2.columns[[1,3]], axis=1)

