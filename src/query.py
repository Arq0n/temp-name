class Query:
    def __init__(self, city: str, zipcode: str, region: str, country: str):
        self._city = city
        self._zipcode = zipcode
        self._region = region
        self._country = country

    def make_location_by_area_query(self) -> dict[str: str]:
        """
        Returns the payload for gasbuddy api using the location of a city
        """
        return {
            "operationName": "LocationByArea",
            "variables": {
                "area": self._city,
                "countryCode": self._country,
                "criteria": {
                    "location_type": [
                        "locality",
                        "metro"
                    ]
                },
                "fuel": 1,
                "regionCode": self._region
            },
            "query": "query LocationByArea($area: String, $countryCode: String, $criteria: Criteria, $fuel: Int, $regionCode: String) {\n  locationByArea(\n    area: $area\n    countryCode: $countryCode\n    criteria: $criteria\n    regionCode: $regionCode\n  ) {\n    counties {\n      countryCode\n      displayName\n      legacyId\n      regionCode\n      __typename\n    }\n    displayName\n    locationType\n    localities {\n      countryCode\n      displayName\n      regionCode\n      __typename\n    }\n    metros {\n      countryCode\n      displayName\n      regionCode\n      __typename\n    }\n    stations(fuel: $fuel) {\n      results {\n        address {\n          country\n          line1\n          line2\n          locality\n          postalCode\n          region\n          __typename\n        }\n        amenities {\n          amenityId\n          name\n          imageUrl\n          __typename\n        }\n        badges {\n          badgeId\n          callToAction\n          campaignId\n          clickTrackingUrl\n          description\n          detailsImageUrl\n          detailsImpressionTrackingUrls\n          imageUrl\n          impressionTrackingUrls\n          internalName\n          targetUrl\n          title\n          __typename\n        }\n        brands {\n          brandId\n          brandingType\n          imageUrl\n          name\n          __typename\n        }\n        emergencyStatus {\n          hasDiesel {\n            nickname\n            reportStatus\n            updateDate\n            __typename\n          }\n          hasGas {\n            nickname\n            reportStatus\n            updateDate\n            __typename\n          }\n          hasPower {\n            nickname\n            reportStatus\n            updateDate\n            __typename\n          }\n          __typename\n        }\n        enterprise\n        fuels\n        hasActiveOutage\n        id\n        latitude\n        longitude\n        name\n        payStatus {\n          isPayAvailable\n          __typename\n        }\n        prices(fuel: $fuel) {\n          cash {\n            nickname\n            postedTime\n            price\n            formattedPrice\n            __typename\n          }\n          credit {\n            nickname\n            postedTime\n            price\n            formattedPrice\n            __typename\n          }\n          discount\n          fuelProduct\n          __typename\n        }\n        priceUnit\n        ratingsCount\n        reviews(limit: 1) {\n          results {\n            agreeTotal\n            canDelete\n            hasAgreed\n            isReportable\n            isVisible\n            memberId\n            overallRating\n            profileImageUrl\n            replyRequested\n            review\n            reviewId\n            reviewDate\n            sentimentScore\n            __typename\n          }\n          __typename\n        }\n        starRating\n        offers {\n          discounts {\n            grades\n            highlight\n            pwgbDiscount\n            receiptDiscount\n            __typename\n          }\n          highlight\n          id\n          types\n          use\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}"
        }

    def make_location_by_zipcode_query(self) -> dict[str: str]:
        """
        Returns the payload for gasbuddy api using a zipcode
        """
        return {
            "operationName": "LocationBySearchTerm",
            "variables": {
                "fuel": 1,
                "maxAge": 0,
                "search": self._zipcode
            },
            "query": "query LocationBySearchTerm($brandId: Int, $cursor: String, $fuel: Int, $lat: Float, $lng: Float, $maxAge: Int, $search: String) {\n  locationBySearchTerm(\n    lat: $lat\n    lng: $lng\n    search: $search\n    priority: \"locality\"\n  ) {\n    countryCode\n    displayName\n    latitude\n    longitude\n    regionCode\n    stations(\n      brandId: $brandId\n      cursor: $cursor\n      fuel: $fuel\n      lat: $lat\n      lng: $lng\n      maxAge: $maxAge\n      priority: \"locality\"\n    ) {\n      count\n      cursor {\n        next\n        __typename\n      }\n      results {\n        address {\n          country\n          line1\n          line2\n          locality\n          postalCode\n          region\n          __typename\n        }\n        badges {\n          badgeId\n          callToAction\n          campaignId\n          clickTrackingUrl\n          description\n          detailsImageUrl\n          detailsImpressionTrackingUrls\n          imageUrl\n          impressionTrackingUrls\n          targetUrl\n          title\n          __typename\n        }\n        brands {\n          brandId\n          brandingType\n          imageUrl\n          name\n          __typename\n        }\n        distance\n        emergencyStatus {\n          hasDiesel {\n            nickname\n            reportStatus\n            updateDate\n            __typename\n          }\n          hasGas {\n            nickname\n            reportStatus\n            updateDate\n            __typename\n          }\n          hasPower {\n            nickname\n            reportStatus\n            updateDate\n            __typename\n          }\n          __typename\n        }\n        enterprise\n        fuels\n        hasActiveOutage\n        id\n        latitude\n        longitude\n             name\n        offers {\n          discounts {\n            grades\n            highlight\n            pwgbDiscount\n            receiptDiscount\n            __typename\n          }\n          highlight\n          id\n       types\n          use\n          __typename\n        }\n        payStatus {\n          isPayAvailable\n          __typename\n        }\n        prices {\n          cash {\n            nickname\n            postedTime\n            price\n            formattedPrice\n            __typename\n          }\n          credit {\n            nickname\n            postedTime\n            price\n            formattedPrice\n            __typename\n          }\n          discount\n          fuelProduct\n          __typename\n        }\n        priceUnit\n        ratingsCount\n        starRating\n        __typename\n      }\n      __typename\n    }\n    trends {\n      areaName\n      country\n      today\n      todayLow\n      trend\n      __typename\n    }\n    __typename\n  }\n}"
        }