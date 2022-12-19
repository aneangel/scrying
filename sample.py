from secrets import API_key
from secrets import URL_sign
import requests

# print(secret.API_key)
# print(secret.URL_sign)

# #gmaps = Client(key = 'API_Key')

lat = 37.9094
lng = 122.6864
fv = 80
pitch = 0

for h in range(0, 360, 45):
    heading = h
    # add time buffer for API

url = "https://maps.googleapis.com/maps/api/streetview?size={size}&location={lattitude},{longitude}&fov={fv}&heading={heading}&pitch={pitch}&key={API_key}&signature={URL_sign}".format(
    size=0, lattitude=lat, longitude=lng, fov=fv, heading=heading, pitch=pitch, API_key=API_key, URL_sign=URL_sign)

# # url = 'https://smrghsh.github.io/360img/images/test.png'


# URL of the image to be downloaded
IMAGE_URL = "https://smrghsh.github.io/360img/images/test.png"

# Open the image from the URL
response = requests.get(IMAGE_URL)

# Save the image to a file
with open("image.jpg", "wb") as f:
    f.write(response.content)
