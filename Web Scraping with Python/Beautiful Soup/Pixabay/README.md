


<p align="center"> <img src="https://www.flaticon.com/svg/vstatic/svg/1406/1406256.svg?token=exp=1619516989~hmac=ab12e2648c941da479ec7ff333efe100" width="200"> </p>
<h1 align="center"> PICTURE MINING FROM PIXABAY PROJECT </h1>

## Context

The aim of this project was to mine 600 different space/space-travel images from Pixabay using Python Programming Language

## Key Features

```python
#Import neccessary models
import requests
import time
import os
from bs4 import BeautifulSoup
from os import path

#Initial page number
page = 1

#Create folder to store pictures
script_dir = "folder path"
os.makedirs(script_dir)

#Login parameters
api_key = 'input your api key'
url_endpoint = "https://pixabay.com/api/"
query = 'space'
per_page = 200
```

## Result:
<p align="center"> <img src="Gif/ezgif.com-gif-maker (space).gif" width="800"></p>



