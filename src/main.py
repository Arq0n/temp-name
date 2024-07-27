import requests

url = "https://www.gasbuddy.com/graphql"

headers = {'Content-Type' : 'application/json',
           'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0'}

payload = {'operationName' : 'LocationBySearchTerm',
           'variables' : {'fuel' : 1, 'maxAge' : 0, 'search' : '92057'},
           'query' : "query LocationBySearchTerm($search: String) { locationBySearchTerm(search: $search) { trends { areaName country today todayLow } } }"
           }
response = requests.post(url=url, headers = headers, json = payload)

print(response.content)
