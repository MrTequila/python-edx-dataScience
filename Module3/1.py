# -*- coding: utf-8 -*-
"""
Created on Fri Nov 04 22:03:21 2016

@author: Michal
"""

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D


matplotlib.style.use("ggplot")

student_dataset = pd.read_csv("Datasets/students.data", index_col=0)

my_series = student_dataset.G3
my_dataframe = student_dataset[["G3","G2","G1"]]

my_series.plot.hist(alpha=0.5)
my_dataframe.plot.hist(alpha=0.5)

student_dataset.plot.scatter(x="G1", y="G3")

fig = plt.figure()
ax = fig.add_subplot(111,projection="3d")
ax.set_xlabel("Final Grade")
ax.set_ylabel("First Grade")
ax.set_zlabel("Daily Alcohol")

ax.scatter(student_dataset.G1, student_dataset.G3, student_dataset["Dalc"],
           c="r", marker=".")
plt.show()