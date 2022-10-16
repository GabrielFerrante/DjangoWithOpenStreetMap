import requests
from random import randint
from django.conf import settings
from django.contrib.gis.geoip2 import GeoIP2
from django.contrib.gis.geoip2 import geoip2 

YELP_SEARCH_ENDPOINT = 'https://api.yelp.com/v3/businesses/search'

#keyword recebe a palavra do serviço buscado e a localização
def yelpSearch(keyword=None, location=None):
    headers = {"Authorization": "Bearer %s" % settings.YELP_API_KEY}

    if keyword and location:
        params = {'term':keyword, 'location':location}
    else:
        params = {'term':'Pizzaria', 'location':'São Paulo'}

    response = requests.get(YELP_SEARCH_ENDPOINT, headers=headers, params=params)

    return response.json()

def getClientCityData():
    geo = GeoIP2()
    ip = get_random_ip()
    try:
        return geo.city(ip)
    except geoip2.errors.AddressNotFoundError:
        return None

def get_random_ip():
    return '.'.join(str(randint(0,255)) for num in range(4))