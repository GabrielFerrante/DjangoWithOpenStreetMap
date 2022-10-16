from django.shortcuts import render
from django.views.generic import View
from .utils import YELP_SEARCH_ENDPOINT, getClientCityData, yelpSearch

class IndexView(View):

    def get(self, request, *args, **kwargs):
        items = []
        city = None
        
        while not city:
            ret = getClientCityData()
            if ret:
                city = ret['city']

        querie = request.GET.get('key', None)
        loc = request.GET.get('loc', None)
        location = city
        context = {
            'city':city,
            'busca':False

        }

        if loc:
            location = loc
        
        if querie:
            items = yelpSearch(keyword=querie, location=location)
            context = {
                'items':items,
                'city':location,
                'busca':True
            }

        return render(request, 'index.html',context)

