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

#import dataset using pandas
dataset = pd.read_csv('iris.csv')

#view the imported dataset by removing '#' present in front of dataset variable
#dataset

#creating a feature matrix which contains set of independent variables
X = dataset.iloc[:, :-1]

#creating a matrix which contains set of dependent variable
Y = dataset.iloc[:, 4]

# Now we can see the two matrix created 'X' which contains independent variables and 'Y' which contains dependent variable
print('\t------------------Matrix X------------------\n\n',X)
print('\n\t------------------Matrix Y------------------\n\n',Y)