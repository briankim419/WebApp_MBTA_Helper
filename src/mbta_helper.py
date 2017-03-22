import urllib.request   # urlencode function
import json


# Useful URLs (you need to add the appropriate parameters for your requests)
from pprint import pprint

GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation?api_key=wX9NwuHnZU2ToO7GmGR9uw&"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"


# A little bit of scaffolding if you want to use it

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """

    # url = "https://maps.googleapis.com/maps/api/geocode/json?address=Prudential%20Tower"
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data



def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """
    url = GMAPS_BASE_URL + '?address=' +place_name
    location = get_json(url)
    latitude =  location['results'][0]['geometry']['location']['lat']
    longitude = location['results'][0]['geometry']['location']['lng']
    return latitude, longitude


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.
    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    example: http://realtime.mbta.com/developer/api/v2/stopsbylocation?api_key=wX9NwuHnZU2ToO7GmGR9
uw&lat=42.352913&lon=-71.064648&format=json
    """
    url = MBTA_BASE_URL + "lat=" + str(latitude) + "&lon=" + str(longitude) + "&format=json"
    mbta_result = get_json(url)
    stop_name= mbta_result['stop'][0]['stop_name']
    distance=mbta_result['stop'][0]['distance']
    return stop_name, distance

def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and the 
    distance from the given place to that stop.
    """
    lat, lng = get_lat_long(place_name)
    return get_nearest_station(lat, lng)

url = "https://maps.googleapis.com/maps/api/geocode/json?address=Prudential%20Tower"
# print(get_json(url))
# print(find_stop_near("PrudentialTower"))
print(find_stop_near('Prudential'))
