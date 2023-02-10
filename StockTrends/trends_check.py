from pytrends.request import TrendReq
import csv
import time 

#Matan Kedar

from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360, backoff_factor= 0.2)
# pytrends = TrendReq(hl='en-US', tz=360, timeout=(None), proxies=['https://35.201.123.31:880',], retries=2, backoff_factor=0.1, requests_args={'verify':False})

all_keywords = ['tsla','aapl','ozsc']
keywords = []
all_stocks = []

winners = []
losers = []

timeframes = ['today 3-m','now 1-d']
            

gprop = ''
x = 1


with open('symbols.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        row = ', '.join(row)
        if row.split(",")[0] != "Symbol":
            all_stocks.append(row.split(",")[0])


with open('symbols2.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        row = ', '.join(row)
        if row.split(",")[0] != "Symbol" and row.split(",")[0] not in all_stocks:
            all_stocks.append(row.split(",")[0])      



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
    # print(data)


    return avg     
    

def searchStock(ticker, x):
    keywords.append(ticker)
    dataList = check_trends(ticker, x) 
    # print(dataList)
    keywords.pop()

    return dataList
 
  
def anomaly():
    y = searchStock(ticker, 0)
    z = searchStock(ticker, 1)
    delta = z - y
    if delta > 40:
        winners.append(ticker)
    else:
        losers.append(ticker)


length = len(all_stocks)
for i in range(0, 30):
    time.sleep(56)
    ticker = all_stocks[i]
    print(ticker)
    anomaly()

for x in range(31, 50):
    time.sleep(6)
    ticker = all_stocks[x]
    print(ticker)
    anomaly()

for x in range(51, 75):
    time.sleep(6)
    ticker = all_stocks[x]
    print(ticker)
    anomaly()


print(winners)
print(losers)
# print(all_stocks)
