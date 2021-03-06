import requests
from pylab import *
import pandas as pd
import os, time
from datetime import datetime

def downloadHistoricalStockQuotes(stock_name):
    base_url = "https://www.google.com/finance/historical"

    stock_qualified_reference = 'NASDAQ:' + stock_name
    payload = {'q':stock_qualified_reference,
               'output':'csv'}

    r = requests.get(base_url, params=payload)

    print r.url

    if r.content is not None:
        fl = open(stock_name+'.csv', 'w')
        fl.write(r.content)
        fl.close()

    r.close()

def getStandardisedQuote(quote_name=None):
    if quote_name in ['AAPL','GOOG']:
        dir_path = ""
        # build file path based on stock-quote
        file_name = quote_name + '.csv'
        file_path = os.path.join(dir_path, file_name)
        stock = pd.read_csv(file_path)

        # renaming columns to overcome corrupt bits in header
        stock.columns = ['Date','Open','High','Low','Close','Volume']

        # Drop duplicate records on same date
        stock = stock.drop_duplicates(cols="Date")

        # parsing <stock> string representing time according to a datetime format
        for i in stock.index:
            stock['Date'][i] = datetime.strptime(stock['Date'][i],"%d-%b-%y")
        #%b date format - Month as locale's abbreviated name.
        # Index stock records on date and drop date from dataframe
        stock.index = stock["Date"]
        del stock["Date"]

        return stock

def getMergedAndFilteredQuotes():
    AAPL = getStandardisedQuote('AAPL')
    GOOG = getStandardisedQuote('GOOG')

    # merging quotes
    DATA = pd.DataFrame({'AAPL':AAPL['Close'], 'GOOG':GOOG['Close']})

    # filtering quotes to discard data before April 1, 2015
    DATA = DATA[DATA.index > datetime(2015,3,31)]

    ## To be implemented: add more attributes to merged frame like year, month
    ## remove date filter : april 1 2015
    ## groupby month and perform mean

    #print DATA.tail(10), len(DATA)

    return DATA

def plotData():
    data = getMergedAndFilteredQuotes()
    #print data.ix[:20].to_string()
    print data.describe()
    print data.corr()
    data.plot(subplots=True)
    show()

def puttingItAllTogether():
    downloadHistoricalStockQuotes('AAPL')
    downloadHistoricalStockQuotes('GOOG')
    plotData()

if __name__ == "__main__":
    #plotData()
    #downloadHistoricalStockQuotes('AAPL')
    puttingItAllTogether()