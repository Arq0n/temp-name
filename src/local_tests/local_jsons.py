import json
from stations import GasStation
j = dict
with open('data_by_city.json', 'r') as infile:
    j = json.load(infile)

GasStation.get_stations_from_json(j['data']['locationByArea']['stations'])

for station in GasStation.sort_by_cheapest(GasStation.REGULAR):
    print(station)

GasStation.clear()

with open('data_by_zipcode.json', 'r') as infile:
    j = json.load(infile)

GasStation.get_stations_from_json(j['data']['locationBySearchTerm']['stations'])

for station in GasStation.sort_by_cheapest(GasStation.REGULAR):
    print(station)
