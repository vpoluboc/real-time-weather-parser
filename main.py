from bs4 import BeautifulSoup
import json
import requests
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
import argparse
import logging
import os
import sys


# Clear the old log file if exists
if os.path.isfile("logs.log"):
    os.remove("logs.log")

###### LOGGING

logger = logging.getLogger(__name__)
logging.basicConfig(filename='logs.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s : %(name)s  : %(levelname)s : %(message)s')

###### PARSE JSON FOR CITY ID USING USER INPUT
with open('city.list.json', 'r', encoding='utf-8') as f:
    cities_data = json.load(f)

city_name = input("Enter the name of the city: ").strip()
logger.info(f'Start parsing json for city ID for the provided name: {city_name}')

city_id = None
for city in cities_data:
    if city['name'].strip().lower() == city_name.lower():  # Case-insensitive and strip spaces
        city_id = city['id']
        break

if city_id is None:
    logger.error(f'City "{city_name}" not found in the list.')
    sys.exit("Error: City not found.")

logger.info(f'Found city ID: {city_id}')
print(f"City ID: {city_id}")

###### GET HTML AND PUSH IT IN WEATHER.HTML WITH DYNAMIC HTML PAGE WITH SELENIUM
options = webdriver.EdgeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)
url = f'https://openweathermap.org/city/{city_id}'
driver.get(url)

time.sleep(3)

html_content = driver.page_source

with open("weather.html", 'w', encoding='utf-8') as f:
    f.write(html_content)

# Properly close the driver
driver.close()
driver.quit()

###### PARSE HTML FOR GET INFO
with open("weather.html", "r", encoding="utf-8") as file:
    page = file.read()

soup = BeautifulSoup(page, "lxml")

try:
    timestamp = soup.find(class_='current-container mobile-padding').find("span").text
    print(f"Timestamp: {timestamp}")
except AttributeError:
    timestamp = "Timestamp not found"
    logger.error("Timestamp not found.")

try:
    city = soup.find(class_='current-container mobile-padding').find("h2").text
    print(f"City: {city}")
except AttributeError:
    city = "City not found"
    logger.error("City not found.")

try:
    temp = soup.find(class_='heading').text.replace("В", " ").strip()
    print(f"Temperature: {temp}")
except AttributeError:
    temp = "Temperature not found"
    logger.error("Temperature not found.")

try:
    alert = soup.find(class_="weather-alert").text.strip()
    print(f"Weather Alert: {alert}")
except AttributeError:
    alert = "No weather alert"
    logger.info("No weather alert found.")

time.sleep(10)
