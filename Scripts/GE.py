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

item_info_dict = {}


def fetch_item_info(item_id):
    item_price = data[item_id]["overall_average"]
    item_name = data[item_id]["name"]
    item_info_dict[item_name] = item_price
    return item_info_dict


# sang, claws, dwh, d pick
item_id_list = ["22481", "13652", "13576", "11920"]
for item in item_id_list:
    fetch_item_info(item)

print(item_info_dict)

csv_file = "C:/Projects/Python/Runescape-Stuff/ItemPrices.csv"
csv_columns = ["Item Name", datetime]

csv_input = pd.read_csv(csv_file, header=0)
csv_input.columns = ["Item", datetime]
csv_input["Item"] = item_info_dict.keys()
csv_input[datetime] = item_info_dict.values()
csv_input.to_csv(csv_file, index=False)

# with open(csv_file, 'w', newline="") as f:
#     writer = csv.writer(f)
#     for key, value in item_info_dict.items():
#         writer.writerow([key, value])


