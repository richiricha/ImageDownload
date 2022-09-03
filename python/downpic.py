#!/usr/bin/python3
import re
import requests
from bs4 import BeautifulSoup
import os
import sys


#site = 'https://www.codespeedy.com/'
#site = sys.argv[1]
site = input("Please provide the site address : ")

response = requests.get(site)
soup = BeautifulSoup(response.text, 'html.parser')
image_tags = soup.find_all('img')
urls = [img['src'] for img in image_tags]
#print(f'URLs { urls }')
#noOfImgs = int(sys.argv[2])
noOfImgs = int(input("Please provide number of images to download : ") or len(urls))

def create_dir(dir):
  if not os.path.exists(dir):
    os.makedirs(dir)
    print("Created Directory : ", dir)
  else:
    print("Directory already existed : ", dir)
  return dir

custDir=create_dir(input("Please provide the download path : ") or 'downloaded_images')

for url in urls[0:noOfImgs]:
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
    if not filename:
         print("Regular expression didn't match with the url: {}".format(url))
         continue
    with open( f'{custDir}/{filename.group(1)}', 'wb') as f:
        if 'http' not in url:
            url = '{}{}'.format(site, url)
        response = requests.get(url)
        f.write(response.content)

print(f"Download complete, downloaded images can be found in {custDir} directory!")
