#!/usr/bin/python

import random
import numpy
import matplotlib.pyplot as plt
import pickle
from sklearn import linear_model
from outlier_cleaner import outlierCleaner


### load up some practice data with outliers in it
ages = pickle.load( open("C:\WorkSpace\MachineLearning\MachineLearning\outliers\practice_outliers_ages.pkl", "r") )
net_worths = pickle.load( open("C:\WorkSpace\MachineLearning\MachineLearning\outliers\practice_outliers_net_worths.pkl", "r") )

### ages and net_worths need to be reshaped into 2D numpy arrays
### second argument of reshape command is a tuple of integers: (n_rows, n_columns)
### by convention, n_rows is the number of data points
### and n_columns is the number of features
ages       = numpy.reshape( numpy.array(ages), (len(ages), 1))
net_worths = numpy.reshape( numpy.array(net_worths), (len(net_worths), 1))
from sklearn.cross_validation import train_test_split
ages_train, ages_test, net_worths_train, net_worths_test = train_test_split(ages, net_worths, test_size=0.1, random_state=42)

### fill in a regression here!  Name the regression object reg so that
### the plotting code below works, and you can see what your regression looks like
reg = linear_model.LinearRegression()
reg.fit(ages_train,net_worths_train)
slope = reg.coef_ ### fill in the line of code to get the right value
print slope
test_score = reg.score(ages_test,net_worths_test) ### fill in the line of code to get the right value
print test_score

#plt.scatter(ages_train,net_worths_train)
#plt.plot(ages_train,reg.predict(ages_train),color='blue',linewidth=3)
#plt.xlabel("ages")
#plt.ylabel("net worth")
#plt.show()

#try:
#    plt.plot(ages, reg.predict(ages), color="blue")
#except NameError:
#    pass
#plt.scatter(ages, net_worths)
#plt.show()


### identify and remove the most outlier-y points
cleaned_data = []
try:
    predictions = reg.predict(ages_train)
    cleaned_data = outlierCleaner( predictions, ages_train, net_worths_train )
    age_cleaned = numpy.array([e[0] for e in cleaned_data])
    net_worth_cleaned = numpy.array([e[1] for e in cleaned_data])
    clf_after_cleaned = linear_model.LinearRegression()
    clf_after_cleaned.fit(age_cleaned,net_worth_cleaned)
    print clf_after_cleaned.coef_
    print clf_after_cleaned.score(ages_test,net_worths_test)
except NameError:
    print "your regression object doesn't exist, or isn't name reg"
    print "can't make predictions to use in identifying outliers"


### only run this code if cleaned_data is returning data
if len(cleaned_data) > 0:
    ages, net_worths, errors = zip(*cleaned_data)
    ages       = numpy.reshape( numpy.array(ages), (len(ages), 1))
    net_worths = numpy.reshape( numpy.array(net_worths), (len(net_worths), 1))

    ### refit your cleaned data!
    try:
        reg.fit(ages, net_worths)
        plt.plot(ages, reg.predict(ages), color="blue")
    except NameError:
        print "you don't seem to have regression imported/created,"
        print "   or else your regression object isn't named reg"
        print "   either way, only draw the scatter plot of the cleaned data"
    plt.scatter(ages, net_worths)
    plt.xlabel("ages")
    plt.ylabel("net worths")
    plt.show()


else:
    print "outlierCleaner() is returning an empty list, no refitting to be done"

