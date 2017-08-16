# -*- coding: utf-8 -*-
"""
Created on Sat Nov 05 15:47:49 2016

@author: Michal
"""

from sklearn.datasets import load_iris
from pandas.tools.plotting import parallel_coordinates, andrews_curves

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib


matplotlib.style.use("ggplot")


data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)

df["target_names"] = [data.target_names[i] for i in data.target]

# Parallel Coordinates Start Here:
plt.figure()
#parallel_coordinates(df, "target_names")
andrews_curves(df, "target_names")
plt.show()
