import requests
import json
from stations import GasStation

def geocode_addr_zip(address: str, zipcode: str) -> tuple[str, str]:
    payload = {"addressdetails": 1, "street": address, "postalcode": zipcode, "format": "jsonv2", "limit": 1}
    headers = {"Referer": "testing"}

    r = requests.get("https://nominatim.openstreetmap.org/search", params=payload, headers=headers)
    data = r.content
    text = data.decode(encoding="utf-8")
    j = json.loads(text)[0]

    coords = (j['lat'], j['lon'])
    return coords

with open('data_by_city.json', 'r') as infile:
    j = json.load(infile)

GasStation.get_stations_from_json(j['data']['locationByArea']['stations'])

"""for station in GasStation.sort_by_cheapest(GasStation.REGULAR):
    address = station._address
    zipcode = station._zip_code.split("-")[0]
    print(station._name + " " + address)

    coords = geocode_addr_zip(address, zipcode)

    print(coords)
"""
print('\n\n')

with open('data_by_zipcode.json', 'r') as infile:
    j = json.load(infile)

GasStation.get_stations_from_json(j['data']['locationBySearchTerm']['stations'])

for station in GasStation.sort_by_cheapest(GasStation.REGULAR):
    address = station._name + " " + station._address
    zipcode = station._zip_code.split("-")[0]
    print(station._name + " " + address)

    coords = geocode_addr_zip(address, zipcode)

    print(coords)



