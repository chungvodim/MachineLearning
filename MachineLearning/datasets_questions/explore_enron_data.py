#!/usr/bin/python
import math
""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("C:/WorkSpace/ud120-projects/final_project/final_project_dataset.pkl", "r"))
count = 0
from_this_person_to_poi = 0
nan=float('nan')
for key, value in enron_data.iteritems():
    #if enron_data[key]["from_this_person_to_poi"] > from_this_person_to_poi:
    #    from_this_person_to_poi = enron_data[key]["from_this_person_to_poi"]
    #    print key
    x = float(enron_data[key]["from_this_person_to_poi"])
    if math.isnan(x) == False :
        if x > from_this_person_to_poi:
            from_this_person_to_poi = x
            print from_this_person_to_poi
            print key
print count

print enron_data['SKILLING JEFFREY K']['from_this_person_to_poi']