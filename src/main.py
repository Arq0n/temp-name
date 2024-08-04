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






city = input("Enter a city; if it contains a spacae, replace with hyphens: ")
zipcode = input("Enter a zipcode: ")

location_by_area_payload = {
    
    "operationName": "LocationByArea",
    "variables": {
        "area": city,
        "countryCode": "US",
        "criteria": {
            "location_type": [
                "locality",
                "metro"
            ]
        },
        "fuel": 1,
        "regionCode": "CA"
    },
    "query": "query LocationByArea($area: String, $countryCode: String, $criteria: Criteria, $fuel: Int, $regionCode: String) {\n  locationByArea(\n    area: $area\n    countryCode: $countryCode\n    criteria: $criteria\n    regionCode: $regionCode\n  ) {\n    counties {\n      countryCode\n      displayName\n      legacyId\n      regionCode\n      __typename\n    }\n    displayName\n    locationType\n    localities {\n      countryCode\n      displayName\n      regionCode\n      __typename\n    }\n    metros {\n      countryCode\n      displayName\n      regionCode\n      __typename\n    }\n    stations(fuel: $fuel) {\n      results {\n        address {\n          country\n          line1\n          line2\n          locality\n          postalCode\n          region\n          __typename\n        }\n        amenities {\n          amenityId\n          name\n          imageUrl\n          __typename\n        }\n        badges {\n          badgeId\n          callToAction\n          campaignId\n          clickTrackingUrl\n          description\n          detailsImageUrl\n          detailsImpressionTrackingUrls\n          imageUrl\n          impressionTrackingUrls\n          internalName\n          targetUrl\n          title\n          __typename\n        }\n        brands {\n          brandId\n          brandingType\n          imageUrl\n          name\n          __typename\n        }\n        emergencyStatus {\n          hasDiesel {\n            nickname\n            reportStatus\n            updateDate\n            __typename\n          }\n          hasGas {\n            nickname\n            reportStatus\n            updateDate\n            __typename\n          }\n          hasPower {\n            nickname\n            reportStatus\n            updateDate\n            __typename\n          }\n          __typename\n        }\n        enterprise\n        fuels\n        hasActiveOutage\n        id\n        latitude\n        longitude\n        name\n        payStatus {\n          isPayAvailable\n          __typename\n        }\n        prices(fuel: $fuel) {\n          cash {\n            nickname\n            postedTime\n            price\n            formattedPrice\n            __typename\n          }\n          credit {\n            nickname\n            postedTime\n            price\n            formattedPrice\n            __typename\n          }\n          discount\n          fuelProduct\n          __typename\n        }\n        priceUnit\n        ratingsCount\n        reviews(limit: 1) {\n          results {\n            agreeTotal\n            canDelete\n            hasAgreed\n            isReportable\n            isVisible\n            memberId\n            overallRating\n            profileImageUrl\n            replyRequested\n            review\n            reviewId\n            reviewDate\n            sentimentScore\n            __typename\n          }\n          __typename\n        }\n        starRating\n        offers {\n          discounts {\n            grades\n            highlight\n            pwgbDiscount\n            receiptDiscount\n            __typename\n          }\n          highlight\n          id\n          types\n          use\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}"
}

response = requests.post(url=url, headers = headers, json = location_by_area_payload)
data = response.content

text = data.decode(encoding = 'utf-8')

j = json.loads(text)

with open("data_by_city.json", "w") as outfile:
    json.dump(j, outfile)

location_by_zipcode_payload = {
    "operationName": "LocationBySearchTerm",
    "variables": {
        "fuel": 1,
        "maxAge": 0,
        "search": zipcode
    },
    "query": "query LocationBySearchTerm($brandId: Int, $cursor: String, $fuel: Int, $lat: Float, $lng: Float, $maxAge: Int, $search: String) {\n  locationBySearchTerm(\n    lat: $lat\n    lng: $lng\n    search: $search\n    priority: \"locality\"\n  ) {\n    countryCode\n    displayName\n    latitude\n    longitude\n    regionCode\n    stations(\n      brandId: $brandId\n      cursor: $cursor\n      fuel: $fuel\n      lat: $lat\n      lng: $lng\n      maxAge: $maxAge\n      priority: \"locality\"\n    ) {\n      count\n      cursor {\n        next\n        __typename\n      }\n      results {\n        address {\n          country\n          line1\n          line2\n          locality\n          postalCode\n          region\n          __typename\n        }\n        badges {\n          badgeId\n          callToAction\n          campaignId\n          clickTrackingUrl\n          description\n          detailsImageUrl\n          detailsImpressionTrackingUrls\n          imageUrl\n          impressionTrackingUrls\n          targetUrl\n          title\n          __typename\n        }\n        brands {\n          brandId\n          brandingType\n          imageUrl\n          name\n          __typename\n        }\n        distance\n        emergencyStatus {\n          hasDiesel {\n            nickname\n            reportStatus\n            updateDate\n            __typename\n          }\n          hasGas {\n            nickname\n            reportStatus\n            updateDate\n            __typename\n          }\n          hasPower {\n            nickname\n            reportStatus\n            updateDate\n            __typename\n          }\n          __typename\n        }\n        enterprise\n        fuels\n        hasActiveOutage\n        id\n        latitude\n        longitude\n             name\n        offers {\n          discounts {\n            grades\n            highlight\n            pwgbDiscount\n            receiptDiscount\n            __typename\n          }\n          highlight\n          id\n       types\n          use\n          __typename\n        }\n        payStatus {\n          isPayAvailable\n          __typename\n        }\n        prices {\n          cash {\n            nickname\n            postedTime\n            price\n            formattedPrice\n            __typename\n          }\n          credit {\n            nickname\n            postedTime\n            price\n            formattedPrice\n            __typename\n          }\n          discount\n          fuelProduct\n          __typename\n        }\n        priceUnit\n        ratingsCount\n        starRating\n        __typename\n      }\n      __typename\n    }\n    trends {\n      areaName\n      country\n      today\n      todayLow\n      trend\n      __typename\n    }\n    __typename\n  }\n}"
}

response = requests.post(url=url, headers = headers, json = location_by_zipcode_payload)
data = response.content

text = data.decode(encoding = 'utf-8')

j = json.loads(text)

with open("data_by_zipcode.json", "w") as outfile:
    json.dump(j, outfile)