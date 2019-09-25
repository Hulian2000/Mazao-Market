import requests

from config import Config

"""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    This file contains the calls to the weather and news API's and how to consume them using requests 
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

# SAMPLE WEATHER API REQUEST
# request = 'http://api.openweathermap.org/data/2.5/weather?q=Kiambu&appid=6d98967004f5e634642db86f5f402d9e'


# Get weather data function
url = Config.RAPID_API_URL

querystring = {"callback": "test", "id": "2172797", "units": "\"metric\" or \"imperial\"",
               "mode": "xml, html, json, text",
               "q": "Kiambu"}

headers = {
    'x-rapidapi-host': Config.RAPID_API_HOST,
    'x-rapidapi-key': Config.RAPID_API_KEY
}


def getWeatherData():
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        print(response)
        return response


""" 
     SAMPLE NEWS API REQUEST
     request = ''     
"""


# Get agricultural news function
def getAgriNews():
    pass


# Get Trending news function
def getTrendingNews():
    pass
