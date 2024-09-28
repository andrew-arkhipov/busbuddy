import urllib
import json

def get_routes(api_key):
    
    #Obtain necessary information from user
    
    origin = input('Where are you? ').replace(' ','+')
    destination = input('Where would you like to go? ').replace(' ','+')
    
    #Set up the URL address
    
    endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
    nav_request = 'origin={}&destination={}&key={}&mode=transit&alternatives=true&transit_routing_preferences=less_walking'.format(origin,destination,api_key)
    request = endpoint + nav_request
    response = urllib.request.urlopen(request).read()       
    directions = json.loads(response)
    
    #Acquire the necessary data from the json response by just getting the route data
    
    routes = directions['routes']
    
    #Iterate through the routes and print specific data for each one
    
    for route_number in range(len(routes)):
        
        try:
            departure_time = routes[route_number]['legs'][0]['departure_time']['text']
            bus_number = routes[route_number]['legs'][0]['steps'][1]['transit_details']['line']['short_name']
            bus_name = routes[route_number]['legs'][0]['steps'][1]['transit_details']['line']['name']
    
            print('\n')
            print(departure_time)
            print(bus_number)
            print(bus_name)
            
        except KeyError:
            print('')
