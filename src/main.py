import requests
import json

url = "https://www.gasbuddy.com/graphql"

headers = {'Content-Type' : 'application/json',
           'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0'}

payload = {'operationName' : 'LocationBySearchTerm',
           'variables' : {'fuel' : 1, 'maxAge' : 0, 'search' : '92057'},
        "query": "query LocationBySearchTerm($brandId: Int, $cursor: String, $maxAge: Int, $search: String) { locationBySearchTerm(search: $search) { stations(brandId: $brandId, cursor: $cursor, maxAge: $maxAge) { count cursor { next __typename } results { fuels id name prices { cash { nickname postedTime price __typename } credit { nickname postedTime price __typename } } } __typename } trends { areaName country today todayLow trend __typename } __typename }}"}

response = requests.post(url=url, headers = headers, json = payload)
data = response.content

text = data.decode(encoding = 'utf-8')

j = json.loads(text)

with open("data.json", "w") as outfile:
    json.dump(j, outfile)

print(response.content)


station_payload = {
    "operationName": "GetStation",
      "variables": {
        "id": "31927"
      },
      "query": "query GetStation($id: ID!) { station(id: $id) prices { credit { nickname postedTime price } } }"
}

station_response = requests.post(url=url, headers=headers, json = station_payload)
station_data = station_response.content

text = station_data.decode(encoding = 'utf-8')

json_data = json.loads(text)

with open("station_data.json", "w") as outfile:
    json.dump(json_data, outfile)

print(station_response.content)



