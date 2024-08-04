from collections import namedtuple
import operator
import functools 

Price = namedtuple('Price', ['cash', 'credit'])

class GasStation:
    REGULAR = 0
    MIDGRADE = 1
    PREMIUM = 2
    DIESEL = 3
    
    stations = dict()
    
    def __init__(self, name: str = None, reg: Price = Price(0,0), mid: Price = Price(0,0),
                 high: Price = Price(0,0) , dis: Price = Price(0,0), addr: str = None, zipc: str = None,
                 region: str = None, id: str = None, lat_long: tuple[float, float] = None):
        if (addr is None):
            raise ValueError("Address is required for each gas station")
        elif (zipc is None):
            raise ValueError("Zip code is required for each gas station")
        self._name = name
        self._address = addr
        self._zip_code = zipc
        self._region = region
        self._regular = reg
        self._midgrade = mid
        self._premium = high
        self._diesel = dis
        self._station_id = id
        self._coords = lat_long
        self.stations[addr] = self

    @staticmethod
    def sort_by_cheapest(type_of_fuel: int, cash: bool = False) -> list['GasStation']:
        'returns a list of gas stations sorted from cheapest to most expensive'
        match type_of_fuel:
            case GasStation.REGULAR:
                type_of_fuel = '_regular'
            case GasStation.MIDGRADE:
                type_of_fuel = '_midgrade'
            case GasStation.PREMIUM:
                type_of_fuel = '_premium'
            case GasStation.DIESEL:
                type_of_fuel = '_diesel'
            case _:
                raise ValueError('type_of_fuel invalid, type given: '+ type_of_fuel)
        valid_stations = [station for station in GasStation.stations.values() if _price_valid(getattr(station, type_of_fuel))]
        return sorted(valid_stations, key=lambda n : getattr(n, type_of_fuel)[0 if cash else 1])

    @classmethod
    def get_stations_from_json(cls, json: 'the stations portion of the dict') -> None:
        'creates station objects from a json'
        json = json['results']
        for station in json:
            cls(
                name = station['name'],
                addr = (station['address']['line1'] + ' ' + station['address']['line2']).strip(),
                zipc = station['address']['postalCode'], 
                region = station['address']['region'] + ", " + station['address']['country'], 
                id = station['id'], 
                lat_long = (station['latitude'], station['longitude']),
                **_get_prices(station))
    @staticmethod
    def clear():
        'clears the stations dictionary'
        GasStation.stations = dict()

    def __str__(self):
        ret = f'{self._name} at {self._address} '
        ret += functools.reduce(operator.add, map(_print_price,['Regular', 'Midgrade', 'Premium', 'Diesel'], [self._regular, self._midgrade, self._premium, self._diesel]))
        ret.removesuffix(', ')
        return ret

    def __rep__(self):
        return f'<GasStation {self.name} at {self.addr}>'
        


def _get_prices(station: "singular station") -> dict[str, Price]:
    'creates a dictionary containing all of the prices of the gas station'
    ret = dict()
    for price in station['prices']:
        cash = price['cash']['price'] if price['cash'] is not None else price['credit']['price']
        credit = price['credit']['price'] if price['credit'] is not None else price['cash']['price']
        cash = cash if cash != 0 else credit
        credit = credit if credit != 0 else cash
        fuel_type = ''
        match price['fuelProduct']:
            case 'regular_gas':
                fuel_type = 'reg'
            case 'midgrade_gas':
                fuel_type = 'mid'
            case 'premium_gas':
                fuel_type = 'high'
            case 'diesel':
                fuel_type = 'dis'
        ret[fuel_type] = Price(cash, credit)
    return ret

def _price_valid(price: Price) -> bool:
    'checks if a price is storing an actual price'
    return price != Price(0,0)

def _print_price(name: str, price: Price) -> str:
    return f'({name} cash: {price.cash}, card: {price.credit}), ' if _price_valid(price) else ''



































