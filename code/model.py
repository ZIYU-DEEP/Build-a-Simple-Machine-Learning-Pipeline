"""
Title: model.py
Description: Conduct model training, testing and evaluation.
Author: Yeol Ye, University of Chicago
"""


from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
import matplotlib.pyplot as plt
import numpy as np
import graphviz


def split(features, target, random_state=0):
    return train_test_split(features, target, random_state=random_state)


def scale(X_train, X_test):
    scaler = MinMaxScaler()
    return scaler.fit_transform(X_train), scaler.transform(X_test)


def tree_classifier(X_train, y_train, max_depth=3):
    return DecisionTreeClassifier(max_depth=max_depth).fit(X_train, y_train)


def plot_decision_tree(clf, feature_names, class_names):
    """
    Plot the decision tree. Credit to University of Michigan.
    This function requires the pydotplus module and assumes it's been installed.

    """
    export_graphviz(clf, out_file="adspy_temp.dot",
                    feature_names=feature_names,
                    class_names=class_names, filled=True, impurity=False)
    with open("adspy_temp.dot") as f:
        dot_graph = f.read()
    return graphviz.Source(dot_graph)


def plot_feature_importances(clf, feature_names):
    c_features = len(feature_names)
    plt.barh(range(c_features), sorted(clf.feature_importances_), color='g', alpha=0.3)
    plt.xlabel("Feature importance")
    plt.ylabel("Feature name")
    plt.yticks(np.arange(c_features), feature_names)
