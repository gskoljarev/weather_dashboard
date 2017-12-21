# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render

from .utils import get_countries, get_current_weather


def index(request):
    countries = get_countries()
    context = {'countries': countries}
    return render(request, 'weather/index.html', context)


def current_weather(request):
    if request.POST:
        query_param = request.POST.get("dropdown")
        data = get_current_weather(query_param)
        context = {
            'capital': data.get("name"),
            'temp': data.get("main").get("temp"),
            'wind_speed': data.get("wind").get("speed"),
        }
        return render(request, 'weather/current_weather.html', context)
