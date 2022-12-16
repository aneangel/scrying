#360-img-viewer
# import urllib.request
import secret
import requests

print(secret.API_key)
print(secret.URL_sign)
# from googlemaps import Client
# import googlemaps
# from googlemaps import convert


# API_key = 'AIzaSyAx4IWLaPkokkFsI3lxC4-gGzohmlaqUYc'
# URL_sign = 'Bmo5bTmryPDHnkGWrIpLUyYgC7k='
# #gmaps = Client(key = 'API_Key')

# lat = 37.9094
# lng = 122.6864

# x,y = 400,400
# size = (x,y)

# #for h in range(0, 360, 45):
# #   heading  = h
# # add time buffer for API

# url = "https://maps.googleapis.com/maps/api/streetview?size=size&location=lat,lng&fov=80&heading=heading&pitch=0&key=API_key&signature=URL_sign"
# # url = 'https://smrghsh.github.io/360img/images/test.png'

# # urllib.request.urlretrieve(url, "local-filename.jpg")

# with open('sample.jpg', 'wb') as f:
#     f.write('url.content')

# URL of the image to be downloaded
# IMAGE_URL = "https://smrghsh.github.io/360img/images/test.png"

# # Open the image from the URL
# response = requests.get(IMAGE_URL)

# # Save the image to a file
# with open("image.jpg", "wb") as f:
#     f.write(response.content)