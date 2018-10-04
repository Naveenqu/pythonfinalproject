# Final Project - North America Travel Assistant

#import all classes and functions
import forecastio
from geopy.geocoders import Nominatim
from robobrowser import RoboBrowser
import csv
from currency_converter import CurrencyConverter 
# pip install --user currencyconverter
import datetime 
from datetime import date 
#import functions file 
import Final_Project_functions

# Ask user for inputs
country = input("What country within North America are you traveling to? ")
city = input("Which city are you travelling to? ")

print(Final_Project_functions.get_current_weather(city))

# creating a list of possible responses
symbol_list={'canada':[],'america':[], 'mexico':[]}
canada = ["canada", "ca", "cad", "can"]
america = ["united states of america", "united states", "usa", "us", "america", "usd"]
mexico = ["mexico", "mehico", "mex", "mxn"]

# webscraping using RoboBrowser
browser = RoboBrowser(parser='html.parser', history=True, user_agent='hh')

# creating a way to output data from webscraping to csv
csv_file = open('data.csv', 'a', newline='')
writer = csv.writer(csv_file) 

# initial stmt for user
print_stmt = ("Here are the top cities you should travel to for your destination")
writer.writerow([print_stmt])
print("Please check file for top cities to visit in",country.title(),'.')

# webscraping depending on which country the user input and writing into csv
if country.lower() in canada:
    browser.open("https://www.tripadvisor.ca/Tourism-g153339-Canada-Vacations.html")
    section_cities=browser.select('span.name')
    for i in section_cities:
        writer.writerow(i)
elif country.lower() in mexico:
    browser.open("https://www.tripadvisor.com/Tourism-g150768-Mexico-Vacations.html")
    section_cities=browser.select('span.name')
    for i in section_cities:
        writer.writerow(i)
elif country.lower() in america:
    browser.open("https://www.tripadvisor.com/Tourism-g191-United_States-Vacations.html")
    section_cities=browser.select('span.name')
    for i in section_cities:
        writer.writerow(i)
else:
    print("Choose a country in North America.")

csv_file.close()


now=datetime.datetime.now()
# determining which country
cur_USD = ["united states of america", "usa", "us", "america", "usd"]
cur_CAD = ["canada", "ca", "cad"]
cur_MXN = ["mexico", "mehico", "mex", "mxn"]


# getting currency for country and printing it
if country.lower() in cur_USD:
    print("Today %d-%d-%d, 100.00 USD will get you" %(now.year,now.month,now.day),Final_Project_functions.currency_data('USD', now), "USD.")
elif country.lower() in cur_CAD:
    print("Today %d-%d-%d, 100.00 USD will get you" %(now.year,now.month,now.day),Final_Project_functions.currency_data('CAD', now), "Canadian Dollars.")
elif country.lower() in cur_MXN:
    print("Today %d-%d-%d, 100.00 USD will get you" %(now.year,now.month,now.day),Final_Project_functions.currency_data('MXN', now), "Mexican Pesos.")
else:
    print("Please choose any country in North America.")
