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


# *******************************************************************
# Split the Data
# *******************************************************************
def split(features, target, random_state=0):
    """
    Split the data into training and testing set.

    Inputs:
        features: (DataFrame)
        target: (DataFrame)
        random_state: (int)

    Returns:
        Four DataFrame objects.
    """
    return train_test_split(features, target, random_state=random_state)


# *******************************************************************
# Scale the Data
# *******************************************************************
def scale(X_train, X_test):
    """
    Split the training and testing data.

    Inputs:
        X_train: (DataFrame)
        X_test: (DataFrame)

    Returns:
        Four DataFrame objects.
    """
    scaler = MinMaxScaler()
    return scaler.fit_transform(X_train), scaler.transform(X_test)


# *******************************************************************
# Build the Model
# *******************************************************************
def tree_classifier(X_train, y_train, max_depth=3):
    """
    Build the decisoin tree model.

    Inputs:
        X_train: (DataFrame)
        X_test: (DataFrame)
        max_depth: (int)

    Returns:
        The DecisionTreeClassifier object
    """
    return DecisionTreeClassifier(max_depth=max_depth).fit(X_train, y_train)


# *******************************************************************
# Plot the Decision Tree
# *******************************************************************
def plot_decision_tree(clf, feature_names, target_name):
    """
    Plot the decision tree. This credits to the University of Michigan.
    This function requires the pydotplus module and assumes it's been
    installed.

    Inputs:
        clf: the model
        feature_names: (list) the list of strings to store feature names
        target_name: (string) the string of the target name

    Returns:
        None
    """
    export_graphviz(clf, out_file="adspy_temp.dot",
                    feature_names=feature_names,
                    class_names=target_name, filled=True, impurity=False)
    with open("adspy_temp.dot") as f:
        dot_graph = f.read()
    return graphviz.Source(dot_graph)


# *******************************************************************
# Plot the Feature Importances
# *******************************************************************
def plot_feature_importances(clf, feature_names):
    """
    Plot the feature importances of the decision tree. This credit to the
    University of Michigan.

    Inputs:
        clf: the model
        feature_names: (list) the list of strings to store feature names

    Returns:
        None
    """
    c_features = len(feature_names)
    plt.barh(range(c_features), sorted(clf.feature_importances_), color='g', alpha=0.3)
    plt.xlabel("Feature importance")
    plt.ylabel("Feature name")
    plt.yticks(np.arange(c_features), feature_names)
