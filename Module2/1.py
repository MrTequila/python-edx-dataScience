# -*- coding: utf-8 -*-
"""
Created on Thu Nov 03 17:51:36 2016

@author: Michal
"""

import pandas as pd


df = pd.read_csv("Datasets/direct_marketing.csv")
print (df[df.recency < 7])