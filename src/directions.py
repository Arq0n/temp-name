import json
import datetime

class Route:
    def __init__(self, units = "metric", distance = None, time = None):
        self._units = units
        self._distance = distance
        self._time = time

    def get_stats_from_json(self, file: 'path of json file') -> None:
        "Store stats from json file into the class"
        j = None
        with open(file, "r") as infile:
            j = json.load(infile)
        if j is not None:
            stats = j["routes"][0]
            self._distance = float(stats["distance"])
            self._convert_to_km()
            self._time = float(stats["duration"])
            self._standardize_time()
        else:
            raise ValueError("Unable to open json file")
    
    def switch_to_imperial(self) -> None:
        "Convert units into imperial units"
        if(self._units == "metric"):
            self._units = "imperial"
            self._distance /= 1.609
        else:
            raise ValueError("Units are already in imperical")
    
    def switch_to_metric(self) -> None:
        "Convert units into metric units"
        if(self._units == "imperial"):
            self._units = "metric"
            self._distance *= 1.609
        else:
            raise ValueError("Units are already in metric")

    def _convert_to_km(self) -> None:
        "Convert meters to kilometers"
        kilometers = self._distance / 1000.0
        if(self._distance > 1000):
            meters = self._distance % 1000.0
            kilometers += meters / 1000.0
        self._distance = kilometers 
        
    def _standardize_time(self) -> None:
        "Put the time in string form"
        seconds = self._time
        time = str(datetime.timedelta(seconds = seconds)).split(":")
        time_in_string = ""
        if(float(time[0]) != 0):
            time_in_string += f"{time[0]} hours "
        if(float(time[1]) != 0):
            time_in_string += f"{time[1]} minutes "
        if(float(time[2]) != 0):
            time_in_string += f"{time[2]} seconds "
        self._time = time_in_string.strip()
    
    def __repr__(self) -> str:
        return f"Distance is approx {self._distance} {"km" if self._units == "metric" else "mi"} in about {self._time}."