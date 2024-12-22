# Weather Parser Script

This Python script allows users to fetch real-time weather information for a specific city using data from OpenWeatherMap. The script dynamically scrapes the weather data from the OpenWeatherMap website, leveraging **Selenium** for browser automation and **BeautifulSoup** for HTML parsing. It provides key weather details such as the current temperature, city name, timestamp, and any active weather alerts.


## Features

- **Real-time weather data**: Retrieves the latest weather information for any city available on OpenWeatherMap.
- **Dynamic Web Scraping**: Uses **Selenium** to interact with a dynamic webpage and fetch weather details.
- **HTML Parsing**: Utilizes **BeautifulSoup** to extract specific data points from the HTML.
- **Error handling**: Gracefully handles missing data and provides logging for troubleshooting.


## Prerequisites

1. **Python 3.6+**  
   Install Python from [python.org](https://www.python.org/downloads/).

2. **Microsoft Edge**  
   Install Microsoft Edge from [microsoft.com/edge](https://www.microsoft.com/edge).

3. **Required Python Libraries**  
   Install dependencies using:
   pip install selenium beautifulsoup4 webdriver-manager