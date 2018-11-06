# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 14:53:31 2018

@author: arkhi
"""

import urllib
import json

endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
api_key = #enter your API key here

origin = input('Where are you? ').replace(' ','+')
destination = input('Where would you like to go? ').replace(' ','+')

nav_request = 'origin={}&destination={}&key={}&mode=transit&alternatives=true&transit_routing_preferences=less_walking'.format(origin,destination,api_key)

request = endpoint + nav_request
response = urllib.request.urlopen(request).read()

directions = json.loads(response)

routes = directions['routes']

for number_of_routes in range(len(routes)):
    
    try:
        departure_time = routes[number_of_routes]['legs'][0]['departure_time']['text']
        bus_number = routes[number_of_routes]['legs'][0]['steps'][1]['transit_details']['line']['short_name']
        bus_name = routes[number_of_routes]['legs'][0]['steps'][1]['transit_details']['line']['name']

        print('\n')
        print(departure_time)
        print(bus_number)
        print(bus_name)
        
    except KeyError:
        print('')

    


#print('\n')
#print(departure_time)
#print(bus_number)
#print(bus_name)
