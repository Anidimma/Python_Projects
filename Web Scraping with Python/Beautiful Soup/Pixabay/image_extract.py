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

#Number of pages to extract
while page <= 3:
    #Login parameters
    api_key = 'input your api key'
    url_endpoint = "https://pixabay.com/api/"
    query = 'space'
    per_page = 200
        
    params = {'q':query, 'per_page':per_page, 'page':page}
    endpoint = url_endpoint+"?key="+api_key

    #Getting the data
    url_links_large = []
    req = requests.get(url=endpoint, params=params)
    data = req.json()

    num_pages = (data['totalHits'] // per_page) + 1

    for image in data['hits']:
        url_links_large.append(image['largeImageURL'])

    print(len(url_links_large))

    #Append the data to a list
    for page in range(2, num_pages+1):
        time.sleep(3)
        params['page'] = page
        req = requests.get(url=endpoint,params=params)
        data = req.json()
        for image in data['hits']:
            url_links_large.append(image['largeImageURL'])

    #Save the data to folder path
    index = 0
    for image in url_links_large:
        index += 1
        r = requests.get(image, allow_redirects=False)
        file_name = "space_image_large" + str(index) + ".jpg"
        abs_file_path = os.path.join(script_dir, file_name)
        open(abs_file_path, 'wb').write(r.content)

    page+=1







