# scrying.py
-------------------------
set of python utilities to download Google Maps Street View images 
and stitch into spherical equi-rectangular projection for WebXR display.

## Setup
-------------------------
first setup an API key through [Google Cloud Platform](https://cloud.google.com/api-keys/docs/get-started-api-keys)
once done change secrets.py to the appropriate key assigned to you.

```
API_key = 'your GCP Google maps key here'

URL_sign = 'your GCP URL sign here'
```
For more information go [Here](https://cloud.google.com/api-keys/docs/create-manage-api-keys)


## Installing Dependencies
-------------------------

```
pip install numpy
pip install imutils
pip install opencv-python
```

## Usage steps
-------------------------

1. Download source images at given latitude and longitude using Google Maps Street View API
```python3 scrying.py 37.123901238 1209380.234144```
2. Stitch the source images into an equirectangular projection using [OpenCV](https://pypi.org/project/opencv-python/)
```python3 stitchTogether.py```

