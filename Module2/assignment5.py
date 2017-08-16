import pandas as pd
import numpy as np


#
# TODO:
# Load up the dataset, setting correct header labels.
#

df = pd.read_csv("Datasets/census.data", names=['education', 'age', 'capital-gain', 'race', 'capital-loss', 'hours-per-week', 'sex', 'classification'])

print df.education.unique()


#
# TODO:
# Use basic pandas commands to look through the dataset... get a
# feel for it before proceeding! Do the data-types of each column
# reflect the values you see when you look through the data using
# a text editor / spread sheet program? If you see 'object' where
# you expect to see 'int32' / 'float64', that is a good indicator
# that there is probably a string or missing value in a column.
# use `your_data_frame['your_column'].unique()` to see the unique
# values of each column and identify the rogue values. If these
# should be represented as nans, you can convert them using
# na_values when loading the dataframe.
#
df["capital-gain"] = pd.to_numeric(df["capital-gain"], errors="coerce")

print df.describe()



#print df
#
# TODO:
# Look through your data and identify any potential categorical
# features. Ensure you properly encode any ordinal and nominal
# types using the methods discussed in the chapter.
#
# Be careful! Some features can be represented as either categorical
# or continuous (numerical). Think to yourself, does it generally
# make more sense to have a numeric type or a series of categories
# for these somewhat ambigious features?
#
ordered_classification = ["<=50K", ">50K"]
df.classification = df.classification.astype("category",
                                             ordered=True,
                                             categories=ordered_classification
                                             ).cat.codes
df = pd.get_dummies(df, columns = ["education","race","sex" ])

#
# TODO:
# Print out your dataframe
#
# .. your code here ..


