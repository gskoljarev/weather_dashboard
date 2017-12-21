from django.conf.urls import include, url


urlpatterns = [
    url(r'^weather/', include('weather.urls')),
]
