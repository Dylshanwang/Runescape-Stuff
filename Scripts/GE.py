import json
from urllib import request
import csv
from datetime import datetime
from pytz import timezone
import pytz
import pandas as pd

# getting Sydney time in string format
time = pytz.timezone('Australia/Sydney')
fmt = '%Y-%m-%d %H:%M:%S'
loc_dt = time.localize(datetime.now())
datetime =loc_dt.strftime(fmt)

# loading in the json and allowing it to be read by dictionary notation
url = "https://rsbuddy.com/exchange/summary.json"
response = request.urlopen(url)
data = json.loads(response.read())

def fetch_item_price(item_id):
    item_price = data[item_id]["overall_average"]
    return item_price


csv_file = "C:/Projects/Python/Runescape-Stuff/ItemPrices.csv"

# appending new price column to csv
# csv_input = pd.read_csv(csv_file)
# csv_input[datetime] = [item_list[0], item_list[1]]
# csv_input.to_csv(csv_file, index=False)
