# scrying.py
-------------------------
Set of python utilities to download Google Maps Street View images and stitch into spherical equirectangular projection for WebXR display.

## Setup
-------------------------
First, set up an API key through [Google Cloud Platform](https://cloud.google.com/api-keys/docs/get-started-api-keys)
Once done, change `API.py` to the appropriate key assigned to you.

```
API_key = 'your GCP Google maps key here'

URL_sign = 'your GCP URL sign here'
```

For more information go [here](https://cloud.google.com/api-keys/docs/create-manage-api-keys)


## Installing Dependencies
-------------------------

```
pip install numpy
pip install imutils
pip install opencv-python
```

## Usage steps
-------------------------
1. git clone repository into following directory ```'\Users\Username\'``` 
2. Download source images at given latitude and longitude using Google Maps Street View API run:
```python3 scrying.py```
3. Stitch the source images into an equi-rectangular projection using [OpenCV](https://pypi.org/project/opencv-python/) run:
```python3 stitchTogether.py```

### Footnotes
-------------------------
After running ```python3 scrying.py``` images folder will be created in the following file path ```'C:\Users\Username\scrying\images'```

* note python scripts use numpy as a dependencies when creating a file for your API keys, avoid naming or using "secrets.py" 
as anaconda3/Lib/secrets.py can (and probably will) get overwritten. Numpy relies on files in this directory called random.py and secrets.py so if you have files with those names numpy will not load.
