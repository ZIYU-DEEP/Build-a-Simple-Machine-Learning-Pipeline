"""
Title: prep.py
Description: The first step: load the data with DataFrame format.
Author: Yeol Ye, University of Chicago
"""

import pandas as pd
import os


SOURCE_PATH = '../data/source/'
PREPARED_PATH = '../data/prepared/'


# *******************************************************************
# Data Type Assigning from Data Dictionary
# *******************************************************************
def type_assignment(column_type):
    """
    This is a helper function for you to specify data type when transforming
    data into DataFrame. This step is inspired by Kunyu He's suggestion.

    It worth nothing that this step is valid only when there exists a
    data dictionary as in this project. If such a dictionary does not exist,
    you should manually check the data type for your data and assign them for
    your pandas DataFrame.

    Inputs:
        column_type (string): the data type of the column
    Return:
        string
    """
    if column_type in ['integer', 'Y/N']:
        return 'int'
    elif column_type in ['percentage', 'real']:
        return 'float'
    return 'object'


# *******************************************************************
# Data Type Assigning from Data Dictionary
# *******************************************************************
def data_transforming(data_file, df_file, dict_file='Data Dictionary.xls'):
    """
    Transform the source csv data into pandas DataFrame, and dump the data
    as a pickle file for later use.

    There are two major operation in this function, the first is to replace
    all the N/A value with the median value, and the second is to set the type
    of each column according to the data dictionary - only when there exists
    a data dictionary!

    Inputs:
        data_file (string): the filename of source data in csv format
        df_file (string): the filename for the output DataFrame
        dict_file (string): the filename of the data dictionary in excel format
    Return:
        None
    """
    df = pd.read_csv(os.path.join(SOURCE_PATH, data_file))

    if dict_file:
        data_dict = pd.read_excel(os.path.join(SOURCE_PATH, dict_file),
                                  header=1)
        column_names = data_dict['Variable Name']
        column_types = data_dict.Type.apply(type_assignment)
        names_types = dict(zip(column_names, column_types))
        df = df.fillna(df.median()).astype(names_types)

    df.to_pickle(os.path.join(PREPARED_PATH, df_file))


# *******************************************************************
# Data Loading from Pickle File
# *******************************************************************
def data_loading(df_file):
    """
    Load the pickled DataFrame file.

    Inputs:
        df_file (string): the filename for the output DataFrame
    Return:
        df (DataFrame): the loaded data in DataFrame format
    """
    df = pd.read_pickle(os.path.join(PREPARED_PATH, df_file))
    return df
