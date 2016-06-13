#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("C:/WorkSpace/MachineLearning/MachineLearning/tools")
from email_preprocess import preprocess
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import numpy as np

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess(words_file = "C:/WorkSpace/MachineLearning/MachineLearning/tools/word_data.pkl", authors_file="C:/WorkSpace/MachineLearning/MachineLearning/tools/email_authors.pkl")




#########################################################
### your code goes here ###
def classify(features_train, labels_train,features_test,labels_test):
    # just training 1% of the full training set
    #features_train = features_train[:len(features_train)/100] 
    #labels_train = labels_train[:len(labels_train)/100] 
    #clf = SVC(kernel="linear")
    clf = SVC(kernel="rbf",C=10000.0)
    t0 = time()
    clf.fit(features_train,labels_train)
    print "training time:", round(time()-t0, 3), "s"
    t0 = time()
    pred = clf.predict(features_test)
    pred_np = np.array(pred)
    print "number of Christ:", pred_np[pred_np == 1].size
    print "prediction time:", round(time()-t0, 3), "s"
    accuracy = accuracy_score(pred, labels_test)
    return accuracy

accuracy = classify(features_train, labels_train,features_test,labels_test)
print accuracy
#########################################################


