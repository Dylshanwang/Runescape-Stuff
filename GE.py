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

# assigning prices to variables
dragon_pick_price = data["11920"]["overall_average"]
sang_staff_price = data["22481"]["overall_average"]
twisted_bow_price = data["20997"]["overall_average"]
dragon_claws_price = data["13652"]["overall_average"]
dragon_warhammer_price = data["13576"]["overall_average"]

item_list = [dragon_claws_price, dragon_warhammer_price]

csv_file = "ItemPrices.csv"

# appending new price column to csv
csv_input = pd.read_csv(csv_file)
csv_input[datetime] = [item_list[0], item_list[1]]
csv_input.to_csv(csv_file, index=False)
