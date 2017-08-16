# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 20:00:24 2016

@author: Michal
"""
import matplotlib as mpl
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np 
import time
from sklearn.svm import SVC
from sklearn import manifold


X = pd.read_csv("Datasets/parkinsons.data", header=0)

y = X['status']
X.drop(labels=["name", "status"], inplace=True, axis=1)

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=7)

from sklearn import preprocessing
#T = preprocessing.Normalizer().fit(X_train)
#T = preprocessing.KernelCenterer().fit(X_train)
#T = preprocessing.MinMaxScaler().fit(X_train)
T = preprocessing.StandardScaler().fit(X_train)
#T = preprocessing.MaxAbsScaler().fit(X_train)


X_train = T.transform(X_train)
X_test = T.transform(X_test)

from sklearn.decomposition import PCA



from sklearn.svm import SVC
#model = SVC()
#model.fit(X_train, y_train)
#score = model.score(X_test, y_test)


C_range = np.arange(0.05,2.01,0.05)
gamma_range = np.arange(0.001, 0.101, 0.001)

best_score = 0
loop_range = np.arange(4,7,1)
l_range = range(2,6,1)
print(l_range)
for x in l_range:
    for n in loop_range:
        #model = PCA(n_components=n)
        model = manifold.Isomap(n_neighbors=x, n_components=n)
        model.fit(X_train)
        
        X_train1 = model.transform(X_train)
        X_test1 = model.transform(X_test)
        for C in C_range:
            for gamma in gamma_range:
                model = SVC(kernel="rbf", C=C, gamma=gamma)
                model.fit(X_train1, y_train)
                score = model.score(X_test1, y_test)
                if score > best_score:
                    best_score = score
        #            print("best: %s",  best_score)

print(best_score)