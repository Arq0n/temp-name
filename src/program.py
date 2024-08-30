import requests
import json
from stations import GasStation
from directions import Route
from query import Query
from geopy.geocoders import Nominatim


URL = "https://www.gasbuddy.com/graphql"
HEADERS = {'Content-Type' : 'application/json', 'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0'}


class Program:
    def __init__(self, curr_loc: str, mpg: str, gallons_to_full: str): 
        self._current_location = curr_loc
        self._mpg = mpg
        self._gallons_to_full = gallons_to_full
        self._start_long_lat = None
    
    def run(self) -> None:
        """
        Runs the class and prints a list of cheapest gas station depending
        on the current location of the user and cost of getting to the 
        station
        """
        location_info = self._get_location_info()
        city = location_info['city'].lower().replace(' ', '-')
        zipcode = location_info['postcode']
        country_code = location_info['ISO3166-2-lvl4'].split('-')[0]
        region_code = location_info['ISO3166-2-lvl4'].split('-')[1]

        curr_query = Query(city, zipcode, region_code, country_code)

        try:
            area_json = json.loads(self._handle_request(URL, HEADERS, curr_query.make_location_by_area_query()))
        except Exception as e:
            print(e.args)
            print(response, text, area_json, end='\n')

        GasStation.get_stations_from_json(area_json['data']['locationByArea']['stations'])
        gas_station_distances = dict()

        for station in GasStation.sort_by_cheapest(GasStation.REGULAR):
            price_to_get_there, full_cost = self._calculate_costs(station, GasStation.REGULAR)
            print(f'{station.__str__()} price to get there: {price_to_get_there}; full cost: {full_cost}')
            gas_station_distances[station.__str__()] = full_cost

        print('\n\n')
        gas_station_distances = dict(sorted(gas_station_distances.items(), key=lambda item: item[1]))

        for station, cost in gas_station_distances.items():
            print(f'{station} total cost: {cost}')

        response = requests.post(url=URL, headers=HEADERS, json=curr_query.make_location_by_zipcode_query())
        text = response.content.decode(encoding = 'utf-8')
        zipcode_json = json.loads(text)

    def _get_location_info(self) -> dict[str: str]:
        """
        Geocodes the user's current position
        Returns a dictionary of the raw information (address, coordinates, etc.) regarding 
        the user's location
        """
        geolocator = Nominatim(user_agent="testing")
        curr_loc = geolocator.geocode(self._current_location)
        coords = f'{curr_loc.latitude}, {curr_loc.longitude}'
        self._start_long_lat = f'{curr_loc.longitude},{curr_loc.latitude}'
        location = geolocator.reverse(coords)
        location_info = location.raw['address']
        return location_info
    
    def _handle_request(self, url: str, headers: dict[str: str], json: dict[str: str] = None) -> str: 
        """
        Sends a post request to the provided url with the given headers and json
        Json parameter sis defaulted to none 
        Returns the decoded response string
        """
        response = requests.post(url=url, headers=headers, json=json)
        return response.content.decode(encoding = 'utf-8')

    def _calculate_costs(self, station: GasStation, gas_type: GasStation.DIESEL | GasStation.REGULAR | \
                            GasStation.MIDGRADE | GasStation.PREMIUM) -> tuple[float, float]:
        """
        Calculate the costs to get to the station provided
        Returns the price to get there and the full cost to fill the tank in a tuple
        """
        station_lat, station_long = station._coords
        dest_long_lat = f'{station_long},{station_lat}'

        osrm_url = f"https://router.project-osrm.org/route/v1/driving/{self._start_long_lat};{dest_long_lat}"
        route_json = json.loads(self._handle_request(osrm_url, HEADERS))

        d = Route()
        d.get_stats_from_json(route_json)
        d.switch_to_imperial()
        
        #implement calculations depending on gas types
        #implement on whether cash or card has better value
        price_to_get_there = d._distance * float(station._regular.cash) / self._mpg
        full_cost = price_to_get_there + self._gallons_to_full * float(station._regular.cash)
        return (price_to_get_there, full_cost)


if __name__ == '__main__':
    current_location = input("Enter your current address: ")
    mpg = float(input("Enter your car's mpg: "))
    gallons_to_full = float(input("Enter approx. gallons needed for a full tank: "))
    p = Program(current_location, mpg, gallons_to_full)
    p.run()