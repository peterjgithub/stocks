from numpy.core.numeric import normalize_axis_tuple
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.dates as mdates

# %matplotlib inline
# from IPython import get_ipython
# get_ipython().run_line_magic('matplotlib', 'inline')
# get_ipython(

# import seaborn as sns
# sns.set(style='darkgrid', context='talk', palette='Dark2')

# my_year_month_fmt. = mdates.DateFormatter('%m/%y')

# data = pd.read_pickle('./data.pkl')
# /Users/peter/GitHub/stocks/us-sp500.csv
# data = pd.read_pickle('./us-sp500.csv')
# data.head(10)

data = pd.read_csv(
    '/Users/peter/GitHub/stocks/us-sp500.csv',
    parse_dates=['Date'],
)



top = 0
topdate = null
floor = 0
floordate = null
bullish = False
bearish = False

def newtop(high, quotedate):
    top = high
    topdate = quotedate

def newfloor(low, quotedate):
    floor = low
    floordate = quotedate

def settopfloor(quotedate, high, low, mvashort, mvalong):
    if (mvalong > mvashort):
        if bearish: #crossover to bullish
            bearish = False
            bullish = True
            newtop(high, quotedate)
        if (high > top):
            newtop(high, quotedate)

    if (mvalong < mvashort):
        if bullish: #crossover to bearish
            bearish = True
            bullish = False
            newfloor(low, quotedate)
        if (low < floor):
            newfloor(low, quotedate)

# High = 120
# Low = 90
# sma = 80

# High = 60
# Low = 50
# sma = 80

data['SMA_250'] = data.iloc[:,1].rolling(window=250).mean()
data['sma250dist'] = data.High - data.SMA_250

print(data.tail(20)) 
