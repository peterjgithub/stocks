# tut2: https://www.youtube.com/watch?v=0e-lsstqCdY&list=PLQVvvaa0QuDcOdF96TBtRtuQksErCEBYZ&index=2
# tut3: https://www.youtube.com/watch?v=QAkOnV1-lIg&list=PLQVvvaa0QuDcOdF96TBtRtuQksErCEBYZ&index=3
# tut4: https://www.youtube.com/watch?v=19yyasfGLhk&list=PLQVvvaa0QuDcOdF96TBtRtuQksErCEBYZ&index=4
# https://pythonprogramming.net/getting-stock-prices-python-programming-for-finance/

# mplfinance is incredible:
# https://github.com/matplotlib/mplfinance/blob/master/README.md

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

import mplfinance as mpf
# from mplfinance import candlestick_ohlc
import matplotlib.dates as mdates

# start = dt.datetime(2000, 1, 1)
# end = dt.datetime.now()
# df = web.DataReader("TSLA", 'yahoo', start, end)
# df.to_csv('tsla.csv')

# df.reset_index(inplace=True)
# df.set_index("Date", inplace=True)
# df = df.drop("Symbol", axis=1)

AdjClose = 'Adj Close'
Open = 'Open'
Volume = 'Volume'
Date = 'Date'

df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)
# df['100ma']=df['Adj Close'].rolling(window=100, min_periods=0).mean()
# df.dropna(inplace=True)

df_ohlc = df[AdjClose].resample('10D').ohlc()
df_volume = df[Volume].resample('10D').sum()
# df_ohlc.reset_index(inplace=True)
df_ohlc[Date] = df_ohlc[Date].map(mdates.date2num)

# print(df_ohlc.head())

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
ax1.xaxis_date()
mpf.plot(df_ohlc, type='candle')

# ax1
# width=2, colorup='g'
# df_ohlc.values

# ax1.plot(df.index, df['Adj Close'])
# ax1.plot(df.index, df['100ma'])
# ax2.bar(df.index, df['Volume'])

# print(df.head())
# print(df.head())
# print(df.tail())
# print(df[['Open', 'High']].head)
# df['Adj Close'].plot()
# plt.show()