from flask import render_template

from app.main import main
from app.requests import getWeatherData


@main.route('/')
def index():
    weatherdata = getWeatherData()
    return render_template('index.html', weatherdata=weatherdata)
