import zipfile
from bs4 import BeautifulSoup
import requests
import re
import webbrowser
import datetime 
import time
from extra import *

web = requests.get("https://www.whoisdownload.com/newly-registered-domains")

soup = BeautifulSoup(web.text,"html.parser")
table = soup.find('table',class_="cart_table table table-striped table-bordered")
tbody = table.find('tbody').find('tr')
file_name = tbody.find('td').text
creation_date = tbody.find('td').findNext('td').findNext('td').text[5::]
current_date = datetime.datetime.now().strftime("%x").replace("/","-")[0:5]
if creation_date==current_date:
    downloaded_file = tbody.find('div',class_="add_cart").find('a').get('href')
    download_file(downloaded_file)
    time.sleep(5)
    print("File downloded!")
    time.sleep(1)
    Unzip()
    print("Done.")
else:
    print("There is no any update file.")


