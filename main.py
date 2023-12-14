import pandas as pd
from pandas import Timestamp as Ts
import json

sampledata = json.load(open('sample.json'))
sampletime = "2023-01-01"


class data:
    def __init__(self, date: pd.Timestamp, price: dict):
        self.date = date
        self.open = price["open"]
        self.close = price["close"]
        self.high = price["high"]
        self.low = price["low"]
        self.timestamp = int(date.timestamp())


d = data(Ts(sampletime), sampledata[sampletime])

historical_data = {
    "timestamps": [],
    "datas": []
}

for x in sampledata:
    d = data(x,sampledata[x])
    historical_date["timestamps"].append(d.timestamp)
    historical_data["datas"].append(data[x])
print(historical_data)