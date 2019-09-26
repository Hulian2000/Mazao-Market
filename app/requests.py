import requests
from config import Config
from app.models import User

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
    response = requests.get(
        f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid=6d98967004f5e634642db86f5f402d9e')
    if response.status_code == 200:
        print(response.json())  # Check the response
        return response.json()


""" 
     SAMPLE NEWS API REQUEST
     request = ''     
"""

# Get agricultural news function
url = "https://search-news-feed.p.rapidapi.com/articles"

querystring = {"title": "Agriculture"}

headers = {
    'x-rapidapi-host': "search-news-feed.p.rapidapi.com",
    'x-rapidapi-key': "7d443101e6msh648b6cd0a0ddc3fp1a860ejsnd8bfd6be3775"
}


def getAgriNews(article):
    source_data = []
    articles_url = 'https://newsapi.org/v2/everything?q={}&apiKey={}'.format(article, Config.API_KEY)
    response = requests.get(articles_url)
    if response.status_code == 200:
        for data in response.json()['articles']:
            source_data.append(data)
            print(source_data)
            return source_data


# Get Trending news function
def getTrendingNews():
    pass
