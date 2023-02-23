
# required imports for this python script

# secrets.py hosts API keys required for google maps API requests
from key import API_key
# # not needed and can be unsigned but if user prefers secrets.py also hosts signature key,
# # encountered errors using URL signature
# from secrets import URL_sign

# # required imports for this python script
import requests
import time
import os

folder_name = "images"
current_dir = os.listdir()

if 'stitchTogether' in current_dir:
    folder_path = os.path.join('stitchTogether', folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"successfully saved images in sub-folder {folder_name} in stitchTogether")
    else:
        print(f"Sub-folder {folder_name} already exists in stitchTogether")

# location variables in terms of longitude and latitude needed for the Google Maps API parameters

lat, lng = 37.3046914,-121.8982429
pitch = 0
#
# # step stops 45 before so 360 + 45, iterative loop to update the heading parameter
# # to pull a full set of static images totaling 360 degrees for image stitching
for h in range(0, 405, 45):
    heading = h
    url = "https://maps.googleapis.com/maps/api/streetview?size=600x300&location={1},{2}&heading={3}&pitch=-0.76&key={0}".format(
        API_key, lat, lng, heading)

    # section of code that will save the pulled images in a previously made with the filename format of
    # latitude-longitude-degree.jpg
    filename = "stitchTogether/images/{0}-{1}-{2}.jpg".format(lat, lng, heading)
    response = requests.get(url)
    with open(filename, "wb") as f:
        f.write(response.content)
    # add time buffer for API
    time.sleep(1)


