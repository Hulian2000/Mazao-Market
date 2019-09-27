import requests

from app.models import User
from config import Config

"""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    This file contains the calls to the weather and news API's and how to consume them using requests
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

user = User.query.all()
for i in user:
    location = i.location
    print(location)


# SAMPLE WEATHER API REQUEST
# request = 'http://api.openweathermap.org/data/2.5/weather?q=Kiambu&appid=6d98967004f5e634642db86f5f402d9e'


# Get weather data function
def getWeatherData():
    # response = requests.get(url, headers=headers, params=querystring)
    location='nairobi'
    response = requests.get(
        f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid=6d98967004f5e634642db86f5f402d9e')
    if response.status_code == 200:
        return response.json()


# Get agricultural news function
def getAgriNews():
    source_data = []
    articles_url = 'https://newsapi.org/v2/everything?q=farming&apiKey={}'.format(Config.API_KEY)
    response = requests.get(articles_url)
    if response.status_code == 200:
        for data in response.json()['articles']:
            source_data.append(data)
        return source_data
