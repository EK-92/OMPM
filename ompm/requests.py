import openmeteo_requests
from openmeteo_sdk.Variable import Variable

from OSMPythonTools.nominatim import Nominatim

nominatim = Nominatim()
city_name = "New York"
city_json = nominatim.query(city_name).toJSON()[0]
latitude = city_json["lat"]
longitude = city_json["lon"]


om = openmeteo_requests.Client()
params = {
    "latitude": latitude,
    "longitude": longitude,
    "hourly": ["temperature_2m", "precipitation", "wind_speed_10m"],
    "current": ["temperature_2m", "relative_humidity_2m"]
}

responses = om.weather_api("https://api.open-meteo.com/v1/forecast", params=params)
response = responses[0]
print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
print(f"Elevation {response.Elevation()} m asl")
print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

# Current values
current = response.Current()
current_variables = list(map(lambda i: current.Variables(i), range(0, current.VariablesLength())))
current_temperature_2m = next(filter(lambda x: x.Variable() == Variable.temperature and x.Altitude() == 2, current_variables))
current_relative_humidity_2m = next(filter(lambda x: x.Variable() == Variable.relative_humidity and x.Altitude() == 2, current_variables))

print(f"Current time {current.Time()}")
print(f"Current temperature_2m {current_temperature_2m.Value()}")
print(f"Current relative_humidity_2m {current_relative_humidity_2m.Value()}")
