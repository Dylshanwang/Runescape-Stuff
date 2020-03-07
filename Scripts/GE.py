import json
from urllib import request
from datetime import datetime
import pytz
import pandas as pd

# getting Sydney time in string format so I can track price over time
time = pytz.timezone('Australia/Sydney')
fmt = '%Y-%m-%d %H:%M:%S'
loc_dt = time.localize(datetime.now())
datetime = loc_dt.strftime(fmt)

# loading in the json data and allowing it to be interpreted in Python via dictionary notation
url = "https://rsbuddy.com/exchange/summary.json"
response = request.urlopen(url)
data = json.loads(response.read())

# defining csv file path and instantiating lists
csv_file = "C:/Projects/Python/Runescape-Stuff/ItemPrices.csv"
item_price_list = []
item_name_list = []


# fetches the data from the json and stores them in lists
def fetch_item_info(item_id):
    item_price_list.append(data[item_id]["overall_average"])
    item_name_list.append(data[item_id]["name"])
    return item_price_list, item_name_list


# sang, claws, dwh, d pick - item names corresponding to id's
item_id_list = ["22481", "13652", "13576", "11920"]
for item in item_id_list:
    fetch_item_info(item)

item_info_list = list(zip(item_name_list, item_price_list))  # creating a list of tuples to pass into the df

# only really used when setting up initially
df = pd.DataFrame(item_info_list, columns=["Item", datetime])
# df.to_csv(csv_file)

csv_input = pd.read_csv(csv_file)  # reading in the csv

#  if you add a new item this adds a new row with the item name
if len(df.index) != len(csv_input.index):
    csv_input = csv_input.append(df.iloc[-1:], sort=False)
    print("Adding {} to the spreadsheet".format(item_name_list[-1]))

# checks if most recent prices are the same as latest in the csv to avoid duplicate columns
if all(df.iloc[:, -1]) != all(csv_input.iloc[:, -1]):

    # adding a new column with most recent prices
    csv_input[datetime] = [item_price_list[0], item_price_list[1], item_price_list[2], item_price_list[3]]
    csv_input.to_csv(csv_file, index=False)
