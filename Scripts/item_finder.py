import json
from urllib import request

url = "https://rsbuddy.com/exchange/summary.json"
response = request.urlopen(url)
data = json.loads(response.read())

print("-------HIGH VOLUME/PRICE-------")

for item in data:
    if data[item]["overall_average"] > 15000000 and data[item]["overall_quantity"] > 10:
        print(data[item]["name"])

print("-------LARGE MARGINS-------")

for item in data:
    margin = data[item]["buy_average"] - data[item]["sell_average"]
    if abs(margin) > 75000 and data[item]["overall_quantity"] > 10:
        print(data[item]["name"])

print("-------LARGE MARGINS/NO VOLUME-------")

for item in data:
    margin = data[item]["buy_average"] - data[item]["sell_average"]
    if abs(margin) > 100000 and data[item]["buy_average"] > 0 and data[item]["sell_average"] > 0:
        print(data[item]["name"])