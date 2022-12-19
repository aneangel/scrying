from secrets import API_key
from secrets import URL_sign
import requests
import time

lat, lng = 37.907921, -122.6869581

pitch = 0

# step stops 45 before so 360 + 45
for h in range(0, 405, 45):
    heading = h
    url = "https://maps.googleapis.com/maps/api/streetview?size=600x300&location={1},{2}&heading={3}&pitch=-0.76&key={0}".format(
        API_key, lat, lng, heading)
    filename = "images/{0}-{1}-{2}.jpg".format(lat, lng, heading)
    response = requests.get(url)
    with open(filename, "wb") as f:
        f.write(response.content)
    time.sleep(1)
    # add time buffer for API

