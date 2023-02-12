import urllib.request
import urllib.parse
import urllib.error
import json

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    # concate the URL + location
    url = serviceurl + urllib.parse.urlencode({'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)  # handle the data from web
    data = uh.read().decode()
    #  read & decode the data from web to UNICODE inside application (from UTF-8)
    print('Retrieved', len(data), 'characters')
    # print how many characters we retrieved...

    try:
        js = json.loads(data)
    except:
        js = None
    # The "try & except" function in Python is used to handle errors and exceptions in your code.
    # It helps your program continue to run, even when something unexpected happens.

    if not js or 'status' not in js or js['status'] != 'OK':
        # in if function are 3 condictions -> is for debuging
        print('==== Failure to retrieve ====')
        print(data)
        continue

    print(json.dumps(js, intent=4))

    # Dig into js format and print out lat & lng for specific location
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat: ', lat, 'lng: ', lng)
    location = js["results"][0]['formatted_address']
    print(location)
