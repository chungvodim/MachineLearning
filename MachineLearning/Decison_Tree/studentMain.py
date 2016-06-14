#!/usr/bin/python

""" lecture and example code for decision tree unit """

import sys
from class_vis import prettyPicture, output_image
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
from classifyDT import classify
from sklearn.metrics import accuracy_score

features_train, labels_train, features_test, labels_test = makeTerrainData()

### the classify() function in classifyDT is where the magic
### happens--fill in this function in the file 'classifyDT.py'!
clf2 = classify(features_train, labels_train, 2)
clf50 = classify(features_train, labels_train, 50)
#### grader code, do not modify below this line

prettyPicture(clf2, features_test, labels_test)
output_image("test.png", "png", open("test.png", "rb").read())
acc_min_samples_split_2 = accuracy_score(clf2.predict(features_test), labels_test)
acc_min_samples_split_50 = accuracy_score(clf50.predict(features_test), labels_test)

print "acc_min_samples_split_2:",round(acc_min_samples_split_2,3)
print "acc_min_samples_split_50:",round(acc_min_samples_split_50,3)