from pytrends.request import TrendReq
import csv

pytrends = TrendReq(hl='en-US')

all_keywords = ['tsla','aapl','ozsc']
keywords = []
all_stocks = []

winners = []
losers = []

timeframes = ['today 3-m','now 1-d']
            
cat = '0'
geo = ''
gprop = ''
x = 1


def check_trends(ticker, x):
    pytrends.build_payload(keywords,
                           cat,
                           timeframes[x],
                           geo,
                           gprop)


    data = pytrends.interest_over_time() 
    mean = round(data.mean(), 2)
    avg = round(data[ticker][-52:].mean(), 2)
    trend = avg/mean[ticker]
    print(data)


    return avg     
    

def searchStock(ticker, x):
    keywords.append(ticker)
    dataList = check_trends(ticker, x) 
    print(dataList)
    keywords.pop()

    return dataList
 
  
def anomaly():
    y = searchStock(ticker, 0)
    z = searchStock(ticker, 1)
    dif = z - y
    if dif > 400:
        winners.append(ticker)
    else:
        losers.append(ticker)

for i in range(0, 2):
    ticker = str(input())
    anomaly()

anomaly()
print(winners)
print(losers)
