
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


# GATHERING DATA FROM 200 SOURCES APART FROM IMAGE DATA 


#Run the extraction multiple times, because the resturants displayed on each page change from time to time
while count <= 5: 
    while current_page < 201:

        url = base_url + loc + '&sortby='+ sorter + '&start=' + str(current_page)
        yelp_r = requests.get(url)
        yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')

        #SPECIFYING WHERE ON THE PAGE PYTHON SHOULD EXTRACT DATA FROM
        general = yelp_soup.findAll(class_ ='arrange-unit__09f24__1gZC1 arrange-unit-fill__09f24__O6JFU border-color--default__09f24__R1nRO')

        print('\n',f'You\'re on count {count} and on page {current_page}','\n')

        for num,biz in enumerate(general):
            if len(biz) > 1:
                for num2,val in enumerate(biz):
                    if num2 == 0:
                        val = str(val)
                        holder = val.split('">(')
                        if len(holder) == 2:
                            
                            val1 = val.split('name=')[1].split('"')[1].replace('&amp;','&')  # Getting the name
                            print(val1)

                            if val.find('aria-label') == -1:
                                val2 = 'NA'
                            else:
                                val2 = val.split('aria-label=')[1].split('"')[1]  # Getting the rating
                            print(val2)

                            container = [val1,val2]
                            hold.append(container)
                            print('\n')
                        
                        elif len(holder) == 1:
                            val1 = val.split('name=')[1].split('"')[1].replace('&amp;','&')  # Getting the name
                            print(val1)

                            if val.find('aria-label') == -1:
                                val2 = 'NA'
                            else:
                                val2 = val.split('aria-label=')[1].split('"')[1]  # Getting the rating
                            print(val2)

                            container = [val1,val2]
                            hold.append(container)
                            print('\n')

        print('\n',f'You left count {count} and page {current_page}','\n')

        current_page += 10

    print('stop')
    current_page = 0
    count += 1



df = pd.DataFrame(hold,columns = columns)
df = df.drop_duplicates(subset= 'Name', keep="first", inplace=False, ignore_index = True) #Dropping Duplicate Entries 
df.to_csv(r'C:/Users/Divinity-PC/Desktop/practice/np_resturants.csv', index=False)


