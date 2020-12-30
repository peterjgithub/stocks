import os
import bs4 as bs
import pickle
import requests
import datetime as dt
import pandas as pd
import pandas_datareader.data as pdr
import yfinance as yf

yf.pdr_override()

FOLDER = 'stockdata'
picklefilepath = FOLDER + '/sp500tickers.pickle'

DATE = 'Date'
OPEN = 'Open'
HIGH = 'High'
LOW = 'Low'
CLOSE = 'Close'
ADJCLOSE = 'Adj Close'
VOLUME = 'Volume'


def update_ticker_stockdata(ticker):

    filepath = FOLDER + '/{}.csv'.format(ticker)
    print('Checking updates for ' + filepath)

    try:
        # reading file with date as index
        # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DatetimeIndex.html
        df = pd.read_csv(filepath, parse_dates=True, index_col=0)
        laststockdata = max(df.index.date)
        print('most recent stockdata in file: ' + str(laststockdata))

        if (laststockdata < dt.date.today()):
            # start = laststockdata # + dt.timedelta(days=1)
            start = dt.datetime(2020, 12, 24)
            # end = dt.datetime.now()
            # end = dt.datetime(2020, 12, 30)
            # print('Requesting stockdata from ' + str(start) + ' to ' + str(end))
            dfupdate = pdr.get_data_yahoo(ticker, start)
            dfupdate.reset_index(inplace=True)
            dfupdate.set_index("Date", inplace=True)
            print(dfupdate.count())
            print(dfupdate)

    except Exception as ex:
        print('Error:', ex)


def get_new_ticker_stockdata(ticker):

    filepath = FOLDER + '/{}.csv'.format(ticker)
    print('Downloading stockdata for new ticker: ' + filepath)
    start = dt.datetime(2000, 1, 1)
    end = dt.datetime.today()

    try:
        df = pdr.get_data_yahoo(ticker, start, end)
        df.reset_index(inplace=True)
        df.set_index("Date", inplace=True)
        df.to_csv(filepath)
        print(df)

    except Exception as ex:
        print('Error:', ex)

        # strPrint = str(df.iloc[-1])
        # print('last line:' + '\n' + strPrint + '\n')

        # strPrint = str(df.iloc[-1].name)
        # print('last line "Name":' + '\n' + strPrint + '\n')

        # strPrint = str(df.index)
        # print('Index:' + '\n' + strPrint)

        # strPrint = str(df.index.date)
        # print('Date Index:' + '\n' + strPrint)

        # strPrint = str(max(df.index.date))
        # print('MaxDate:' + '\n' + strPrint)
        # strPrint = df.iloc[-1].DatetimeIndex.year
        # print('last line "Name":' + '\n' + strPrint + '\n')

        # reading file without date index
        # df = pd.read_csv(filepath)

        # strPrint = str(df.iloc[-1])
        # print('last line:' + '\n' + strPrint + '\n')

        # strPrint = df[DATE].iat[-1] #iat is prefered for requesting a value
        # print('last update:' + '\n' + strPrint + '\n')

        # strPrint = str(df.iloc[-1].name)
        # print('last line "Name":' + '\n' + strPrint + '\n')


def update_tickers():

    print('update tickerlist')

    tickers = []

    resp = requests.get(
        'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, "lxml")
    table = soup.find('table', {'class': 'wikitable sortable'})
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text.strip()
        tickers.append(ticker)

    with open(picklefilepath, "wb") as f:
        pickle.dump(tickers, f)

    return tickers


def load_tickers():

    tickers = []

    try:
        mod_timestamp = dt.datetime.fromtimestamp(os.path.getmtime(picklefilepath))
        if (dt.datetime.now() - mod_timestamp).days <= 1:
            with open(picklefilepath, "rb") as f:         
                tickers = pickle.load(f)
        else:
            tickers = update_tickers()
        return tickers

    except IOError:
        return update_tickers()

    except pickle.UnpicklingError:
        os.remove(picklefilepath)
        return update_tickers()

    except Exception as ex:
        print('*** Error *** \n', ex)

def run_updater():

    if not os.path.exists(FOLDER):
        os.makedirs(FOLDER)

    tickers = load_tickers()

    for ticker in tickers[:4]:
        filepath = FOLDER + '/{}.csv'.format(ticker)
        print( '\n>>> ' + filepath)
        if not os.path.exists(filepath):
            get_new_ticker_stockdata(ticker)
        else:
            update_ticker_stockdata(ticker)

run_updater()
