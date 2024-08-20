import requests
import json
from stations import GasStation
from directions import Route
from query import Query
from geopy.geocoders import Nominatim


url = "https://www.gasbuddy.com/graphql"
headers = {'Content-Type' : 'application/json', 'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0'}

current_location = input("Enter your current address: ")
geolocator = Nominatim(user_agent="testing")
curr_loc = geolocator.geocode(current_location)
coords = f'{curr_loc.latitude}, {curr_loc.longitude}'
location = geolocator.reverse(coords)
location_info = location.raw['address']

city = location_info['city'].lower().replace(' ', '-')
zipcode = location_info['postcode']
country_code = location_info['ISO3166-2-lvl4'].split('-')[0]
region_code = location_info['ISO3166-2-lvl4'].split('-')[1]

curr_query = Query(city, zipcode, region_code, country_code)

response = requests.post(url=url, headers=headers, json=curr_query.make_location_by_area_query())
text = response.content.decode(encoding = 'utf-8')
area_json = json.loads(text)


response = requests.post(url=url, headers=headers, json=curr_query.make_location_by_zipcode_query())
text = response.content.decode(encoding = 'utf-8')
zipcode_json = json.loads(text)

print(zipcode_json)