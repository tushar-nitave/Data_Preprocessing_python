#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 09:12:15 2017

@author: tnitave
"""

#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as pt

#--------------------Importing Data and Creating Matrix

dataset = pd.read_csv('iris.csv')

X = dataset.iloc[:, :-1]

Y = dataset.iloc[:, 4]

#--------------------Dealing with missing data---------------------
from sklearn.preprocessing import Imputer

imputer  = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:,0:4])
X[:,0:4] = imputer.transform(X[:,0:4])