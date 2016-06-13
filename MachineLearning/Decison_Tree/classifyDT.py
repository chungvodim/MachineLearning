from sklearn import tree
def classify(features_train, labels_train):
    clf = tree.DecisionTreeClassifier()
    clf.fit(features_train, labels_train)
    return clf