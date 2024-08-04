from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import requests
import json
from stations import GasStation

with open('data_by_city.json', 'r') as infile:
    j = json.load(infile)

GasStation.get_stations_from_json(j['data']['locationByArea']['stations'])

for station in GasStation.sort_by_cheapest(GasStation.REGULAR):
    address = station._address
    zipcode = station._zip_code.split("-")[0]
    print(address)

    geolocator = Nominatim(user_agent="test")
    geocode = RateLimiter(lambda query: geolocator.geocode(f"%s, {station._region}" % query), min_delay_seconds=1)
    location = geocode(address)
    coords = (location.latitude, location.longitude)

    print(coords)

print('\n\n')
with open('data_by_zipcode.json', 'r') as infile:
    j = json.load(infile)

GasStation.get_stations_from_json(j['data']['locationBySearchTerm']['stations'])

for station in GasStation.sort_by_cheapest(GasStation.REGULAR):
    address = station._address
    print(address)