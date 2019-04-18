"""
Title: prep.py
Description: Load the data for the project.
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
    """
    df = pd.read_csv(os.path.join(SOURCE_PATH, data_file))

    if dict_file:
        data_dict = pd.read_excel(os.path.join(SOURCE_PATH, dict_file),
                                  header=1)
        types = data_dict.Type.apply(type_assignment)
        data_types = dict(zip(data_dict['Variable Name'], types))
        df.fillna(df.median(), inplace=True)
        df = df.astype(data_types)

    df.to_pickle(os.path.join(PREPARED_PATH, df_file))


# *******************************************************************
# Data Loading from Pickle File
# *******************************************************************
def data_loading(df_file):
    """
    Load the pickled DataFrame file.
    """
    df = pd.read_pickle(os.path.join(PREPARED_PATH, df_file))
    return df
