# library of functions 

import forecastio
from geopy.geocoders import Nominatim
from currency_converter import CurrencyConverter 
# pip install --user currencyconverter
import datetime 
from datetime import date 

# Get weather update 
def get_current_weather(address):
	api_key="225f7156d4473ed0732a45f3c845c469"
	geolocator = Nominatim()
	location = geolocator.geocode(address)
	if location:
		forecast = forecastio.load_forecast(api_key, location.latitude, location.longitude)
		current_forecast = forecast.currently()
		return f"In {location.address} the current weather is {current_forecast.summary} and temperature is {current_forecast.temperature}."
	else:
		return "Location not found. Try again."

#Using latest data for currency conversion rates  
cur_conv = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip') 
#defining function to write currency conversion to file 
def currency_data(country, now):
	return round(cur_conv.convert(100, 'USD', country),2)	 
	#, date=date(now.year, now.month, now.day)
