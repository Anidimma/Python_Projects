

<p align="center"> <img src="https://images.unsplash.com/photo-1414235077428-338989a2e8c0?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80" width="500" /> </p>
<h1 align="center"> RESTUARANT DESCRIPTION WEB SCRAPING PROJECT </h1>

## Context

The aim of this project was to scrape the description of the Restaurants at New Port Beach, California. This data was scraped from yelp.com using python programming language

## Key Features

```python
#IMPORTING THE MODULES
import requests
from bs4 import *
import pandas as pd 


columns = ['Name','Rating']
hold = []
       

# SPECIFYING HOW THE CODE SHOULD ACCESS THE WEBSITE
"""To understand how the variables under work with the code please
go to 'www.yelp.com' search for 'Resturants' and for location put 'Newport Beach, CA'
after that you will be taken to a new webpage, observe the url of that
web page then you'll understand how the codes below work with the defined variables"""

base_url = 'https://www.yelp.com/search?find_desc=Restaurants&find_loc=' # Initial url
loc = 'Newport Beach, CA' # Specifying the city
sorter = 'recommended'
current_page = 0
count = 0
```

## Result:
<p align="center"> <img src="Gif/ezgif.com-gif-maker.gif" width="800"></p>



