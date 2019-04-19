"""
Title: feature.py
Description: Conduct feature engineering.
Author: Yeol Ye, University of Chicago
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# *******************************************************************
# Cut the Outliers
# *******************************************************************
def cut_outliers(data, col_name):
    """
    Filter out the outliers in a column of the data.

    Inputs:
        data: (DataFrame) the full data
        col_name: (string) the name of the column in need of cut outliers

    Returns:
        data: (DataFrame) the updated full data
    """
    col = data[col_name]
    data = data[np.abs(col-col.mean()) <= (3 * col.std())]
    return data


# *******************************************************************
# Discretize Continuous Features
# *******************************************************************
def discretize(data, bins, list_to_discrete):
    """
    Discretize the value of certain columns (specified in list_to_discrete)
    in the full data. Note that this function transforms data in place.

    Inputs:
        data: (DataFrame) the full data
        bins: (int) the bins to discretize the column. For example, if bins
            is 3, then the values of the data are cut into 3 ranges in order,
            and are transformed to 0, 1 and 2 according to its original value.
        list_to_discrete: (list) the list storing the name of columns to be
            discretized.

    Returns:
        None
    """
    for col_name in list_to_discrete:
        data[col_name] = pd.cut(data[col_name], bins, right=True,
                                precision=4).cat.codes


# *******************************************************************
# Convert the Categorical to Dummies
# *******************************************************************
def one_hot_encoding(data, list_to_dummy):
    """
    Convert categorical columns into dummy/indicator columns and drop the
    original categorical columns.

    Inputs:
        data: (DataFrame) the full data
        list_to_discrete: (list) the list storing the name of columns to be
            one-hot encoded.

    Returns:
        data: (DataFrame) the transformed full data
    """
    for col_name in list_to_dummy:
        df_dummy = pd.get_dummies(data[var], prefix=col_name)
        data = pd.concat([data, df_dummy], axis=1).drop(col_name, axis=1)
    return data