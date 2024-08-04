import geocoder
import requests 


g = geocoder.ip('me')
print(g.latlng)

response = requests.get('http://ipinfo.io')
print(response.json()['loc'])