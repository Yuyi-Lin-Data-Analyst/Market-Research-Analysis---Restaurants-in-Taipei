#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 16:15:07 2022

@author: yuyi
"""

import pandas as pd
from bs4 import BeautifulSoup
import requests
import re
from time import sleep
import csv

# to get the category list to fetch datas under each category

#fetch data from ifoodie_taipei city
url = 'https://ifoodie.tw/explore/%E5%8F%B0%E5%8C%97%E5%B8%82/list' 

response = requests.get(url, verify=False)
soup = BeautifulSoup(response.content, "html.parser")
   
cards = soup.find_all(
    "a", {"class":"jsx-1377605966 btn"}, href=True)

# key: name, value: url
category_list={} 

for card in cards:
    category_list[card.text] = card['href']

# delete the unesessary fetched data    
unwanted_keys = ['台北市', '新北市', '桃園市', '基隆市', '新竹市', '新竹縣', 
 '台中市', '苗栗縣', '彰化縣', '南投縣', '雲林縣', '高雄市', 
 '台南市', '嘉義市', '嘉義縣', '屏東縣', '宜蘭縣', '花蓮縣', '台東縣']

for key in unwanted_keys:
    category_list.pop(key, None)


#fetch taipei city restaurant data 

data = {} #store all the fetched data in the dictionary 
title = [] #store restaurant names in the list
review_row = [] #review row b4 clean
review_row_nums = [] #review row after clean
address = [] #address of the restaurant
categories = [] #cruisine/meal types

home_url = 'https://ifoodie.tw'
    

#loop over the category list to automatically get data from all category pages
for c_name, c_link in category_list.items():
    
    #ifoodie website can only display maximum 67 pages per category
    for page in range(1, 68):
        
        
        try:    
            response = requests.get(home_url +  c_link + '?page=' + str(page), verify=False)
            soup = BeautifulSoup(response.content, "html.parser")
            
            cards = soup.find_all(
                'div', {'class': 'jsx-3292609844 restaurant-info'}) 
            
        
            for card in cards:
            
                title.append(card.find(  # 餐廳名稱
                    "a", {"class": "jsx-3292609844 title-text"}).getText())
                
                
                review_row.append(card.find( #rating, review_count, avg_price
                    "div", {"class": "jsx-3292609844 review-row"}).getText())
               
                
            
                address.append(card.find(  # 餐廳地址
                    "div", {"class": "jsx-3292609844 address-row"}).getText())
                
                
                # each restaurant has multiple categories, 
                # therefore I loop over the categories and store all of them into list
                items = [] 
                
                for category in card.find_all('a', attrs={"class":"jsx-3292609844 category"}):
                    items.append(category.get_text())
                
                # to elimenate the first element in the category list - '附近餐廳'
                categories.append(items[1:])
                
            # to see the current progress
            print(c_name, page)
        
            # to not overwelm the website and prevent IP getting blocked
            sleep(3)
         
        # if the current category don't have that many page, 
        # it hit break and continue with the next category   
        except:
            print('break')
            break
        
# to clean up the review row
for r in review_row:
    review_row_nums.append(re.findall(r"\b\$?[\d,.]+", r))
        

# save data into dictionary and later use the keys to be column name
data['title'] = title
data['review_row_nums'] = review_row_nums
data['address'] = address
data['categories'] = categories


# convert the dictionary to dataframe
data_df = pd.DataFrame.from_dict(data)

# store data into csv file
data_df.to_csv('ifoodie.csv', index=False)

 
