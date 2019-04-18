"""
Title: explore.py
Description: Conduct data visualization and explore their distributions.
Author: Yeol Ye, University of Chicago
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# *******************************************************************
# Generate Count Plots for Categorical Data
# *******************************************************************
def count_plot(col_name, data, title):
    """
    Draw a count plot for one column of the data.

    Inputs:
        col_name: (string) the name of a certain column of the data
        data: (DataFrame) the data
    Returns:
        None
    """
    plt.figure()
    ax = sns.countplot(x=col_name, data=data, palette="Set3")
    ax.set_title(title)


# *******************************************************************
# Generate Distribution Plots for Categorical Data
# *******************************************************************
def dist_plot(data, cut=True):
    """
    Draw a distribution plot for every column of the data.

    Inputs:
        data: (DataFrame) the data
        cut: (bool) if True, the values of data lower than 0.05 or higher than
        0.95 quantile will be filtered out; else there will be no filtering.
    Returns:
        None
    """
    n_cols = data.shape[1]
    fig_cols = 2
    fig_rows = n_cols // fig_cols
    fig, axes = plt.subplots(nrows=fig_rows, ncols=fig_cols,
                             figsize=[20, fig_rows * 4])

    for i, col_name in enumerate(data.columns):
        subdata = data[col_name]
        if cut:
            _range = (subdata >= subdata.quantile(0.05)) & (
                        subdata < subdata.quantile(0.95))
            subdata = subdata[_range]
        sns.distplot(subdata, ax=axes[i // fig_cols, i % fig_cols], color='g')


# *******************************************************************
# Generate HeatMap for Features
# *******************************************************************



