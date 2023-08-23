# -*- coding: UTF-8 -*-

import requests
import json
from datetime import datetime


# FUNCTIONS
def request(url):
    respose = requests.get(url)
    return json.loads(respose.text)


# READ DATA
## history data
url_history = ('https://api.coincap.io/v2/assets/bitcoin/history?' +
        'interval=d1&' +
        'start=1534820400000&'+ 
        'end=1692576000000')
data_history = request(url_history)

## candles data
url_candles = ('https://api.coinmarketcap.com/data-api/v3.1/cryptocurrency/historical?'+
        'id=1&'+
        'convertId=2783&'+
        'timeStart=1690070400&'+
        'timeEnd=1692748800&'+
        'interval=1d')
data_candles = request(url_candles)

# MANIPULATION
for i in data_history['data']:
    priceUsd = i['priceUsd']
    time = i['time']
    date = i['date']

for i in data_candles['data']['quotes']:
    high = i.get('quote', '').get('high')
    low = i.get('quote', '').get('low')
    open = i.get('quote', '').get('open')
    close = i.get('quote', '').get('close')
    volume = i.get('quote', '').get('volume')
    marketCap = i.get('quote', '').get('marketCap')

    time = i.get('quote', '').get('timestamp')
    dt_object = datetime.strptime(time, "%Y-%m-%dT%H:%M:%S.%fZ")

    year = dt_object.year
    month = str(dt_object.month).zfill(2) if len(str(dt_object.month)) == 1 else dt_object.month
    day = str(dt_object.day).zfill(2) if len(str(dt_object.day)) == 1 else dt_object.day

# WRITE DATA