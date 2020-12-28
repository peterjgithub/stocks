# pandas: https://realpython.com/pandas-dataframe/#introducing-the-pandas-dataframe
# panda wrangling: https://github.com/pandas-dev/pandas/blob/master/doc/cheatsheet/Pandas_Cheat_Sheet.pdf

# 1. Dictionaries / lists

# CHANGEABLE List is a collection which is ORDERED and CHANGEABLE. Allows DUPLICATE members.
# mylist = ["apple", "banana", "cherry", "apple", "cherry"]

# unCHANGEABLE Tuple is a collection which is ORDERED and unCHANGEABLE. Allows DUPLICATE members.
# thistuple = ("apple", "banana", "cherry", "apple", "cherry")

# unCHANGEABLE Set is a collection which is unORDERED and unindexed. NO-DUPLICATE members.
# thisset = {"apple", "banana", "cherry", "apple"}

# CHANGEABLE Dictionary is a collection which is unORDERED and CHANGEABLE. NO-DUPLICATE members.
# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }

# 2. Numpy arrays
# >  Your data is 2-dimensional (or higher)
# > numerical/mathematical calculations

# 3. Pandas series / dataframes
# > merge multiple data sets
# > import data from or export data


import pandas as pd
import numpy as np

df = pd.read_csv(
    '/Users/peter/GitHub/stocks/us-sp500.csv',
    parse_dates=['Date'],
)
# index

print("dataframe info:")
print(df.info())

print("dataframe Volume of row 0:")
print(df['Volume'][0])

print("dataframe:")
print(df)


print("AdjClose:")
print(df.AdjClose)