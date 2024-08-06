import requests
import json
from directions import Route

"""
OSRM uses longitude, latitude in the url 
-117.840161,33.642947 is UCI for example
could've confused longitude and latitude :/
"""

start_long_lat = input("longitude, latitude: ")
dest_long_lat = input("longitude, latitude: ")

url = f"https://router.project-osrm.org/route/v1/driving/{start_long_lat};{dest_long_lat}"

headers = {'Content-Type' : 'application/json', 'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0'}


"""
Function to send request to url with headers
Payload is optional and returns decoded content as a dict
"""
def send_request(url: str, headers: str, payload: str = None) -> dict[str: str]:
    response = None
    try:
        if(payload != None):
            response = requests.post(url = url, headers = headers, json = payload)
        else:
            response = requests.post(url=url, headers = headers)
        text = response.content.decode(encoding = 'utf-8')
        json_response = json.loads(text)
        return json_response
    except:
        print("Error in sending request and receiving response")
    
response = send_request(url, headers)

"""
routing.json contains fastest route (in theory idk if its practical)
duration is in seconds and distance is in meters 
"""
with open("routing.json", "w") as outfile:
    json.dump(response, outfile)

"""
Test coords
-117.840161,33.642947
-117.701242491603,33.654875498759
"""

d = Route()
d.get_stats_from_json("routing.json")
d.switch_to_imperial()
print(d)
d.switch_to_metric()
print(d)