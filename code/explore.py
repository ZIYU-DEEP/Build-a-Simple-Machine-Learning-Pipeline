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
        title: (string) the title set for your plot

    Returns:
        None
    """
    sns.set(style='whitegrid')
    plt.figure()
    ax = sns.countplot(x=col_name, data=data, palette="Set3")
    ax.set_title(title)


# *******************************************************************
# Generate Plots for Numeric Data to Detect Distribution & Separability
# *******************************************************************
def dist_plot(data, cut=True):
    """
    Draw a distribution plot for every column of the data.

    Inputs:
        data: (DataFrame) the data containing features (only numeric)
        cut: (bool) if True, the values of data lower than 0.05 or higher than
        0.95 quantile will be filtered out; else there will be no filtering.

    Returns:
        None
    """
    sns.set(style='whitegrid')
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
    sns.despine()


def box_plot(data):
    """
    Draw a box plot for every column of the data.

    Inputs:
        data: (DataFrame) the data containing features (only numeric)

    Returns:
        None
    """
    sns.set(style='whitegrid')
    n_cols = data.shape[1]
    fig_cols = 2
    fig_rows = n_cols // fig_cols
    fig, axes = plt.subplots(nrows=fig_rows, ncols=fig_cols,
                             figsize=[20, fig_rows * 4])

    for i, col_name in enumerate(data.columns):
        subdata = data[col_name]
        sns.boxplot(subdata, ax=axes[i // fig_cols, i % fig_cols], color='g')


def pair_plot(data, target_name):
    """
    Draw the pair plot and see the separability of features for the data.
    Different points with different target values are denoted by different colors.

    Inputs:
        data: (DataFrame) the data containing features (only numeric)
        target_name: (string) the column name of the target

    Returns:
        None
    """
    sns.pairplot(data, size=3, hue=target_name, palette='husl')


# *******************************************************************
# Generate Correlation Matrix for Features to study Correlations
# *******************************************************************
def corr_plot(data):
    """
    Draw a correlation matrix for the data. This function is credit to the
    official document of Seaborn (https://seaborn.pydata.org/examples/many_pai
    rwise_correlations.html).

    Inputs:
        data: (DataFrame) the data containing features (only numeric)

    Returns:
        None
    """
    sns.set(style='white')
    corr = data.corr()
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True
    f, ax = plt.subplots(figsize=(11, 9))
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    sns.heatmap(corr, mask=mask, cmap=cmap, vmax=1, center=0, annot=True,
                fmt='.2f', square=True, linewidths=.5, cbar_kws={"shrink": .5})
    ax.set_title('The Correlation Matrix')


# *******************************************************************
# Drop Some Features with High Correlations to Others
# *******************************************************************
def drop_redundancy(data, col_names):
    """
    Drop the columns with high correlation to an existing column.

    Inputs:
        data: (DataFrame) the data storing feature columns
        col_names: (list) the name of columns to be dropped

    Returns:
        data: (DataFrame) the cleaned data
    """
    data = data.drop(col_names, axis=1)
    return data
