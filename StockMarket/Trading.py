# Alpha Vantage API Key: 5TC8BQSVXADIOJIA

from yahoo-finance import Share
from pprint import pprint
from alpha_vantage.timeseries import TimeSeries
import sys
import random

ticker="aapl";
lines = str("5TC8BQSVXADIOJIA");
key=random.choice(lines);
time=TimeSeries(key=key, output_format="pandas");
data=time.get_intraday(symbol=ticker, interval="1min", outputsize='full');
print(ticker);
print(data);