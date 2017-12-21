# -*- coding: utf-8 -*-

import requests

from django.conf import settings


def get_countries():
    API_URL = 'https://restcountries.eu/rest/v2/all'
    response = requests.get(API_URL)
    return response.json()


def get_current_weather(query_param):
    API_URL = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'APPID': settings.OWM_API_KEY,
        'q': query_param,
    }
    response = requests.get(API_URL, params=params)
    return response.json()