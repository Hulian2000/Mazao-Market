from flask import render_template

from app.main import main
from app.requests import getWeatherData

weatherdata = getWeatherData()


@main.route('/')
def index():
    return render_template('index.html', weatherdata=weatherdata)


@main.route('/weather')
def weather():
    return render_template('weather_data.html', weatherdata=weatherdata)
