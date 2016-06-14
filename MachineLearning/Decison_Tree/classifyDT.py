from sklearn import tree
def classify(features_train, labels_train, min_samples_split):
    clf = tree.DecisionTreeClassifier(min_samples_split = min_samples_split)
    clf.fit(features_train, labels_train)
    return clf