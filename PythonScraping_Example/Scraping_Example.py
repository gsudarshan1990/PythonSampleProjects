import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime


url='https://login.yahoo.com/'

response=requests.get(url)
soup=BeautifulSoup(response.content,'html.parser')
name_box=soup.find('h1',attrs={'class':'sign-in-title-greeting'})
print(name_box.text.strip())
sign_in_text=name_box.text.strip()

trouble_sign_in=soup.find('a',attrs={'id':'mbr-forgot-link'})
print(trouble_sign_in.text.strip())
trouble_sign_in_text=trouble_sign_in.text.strip()

with open('C:/Users/EP833WG/Desktop/python_read_files/data_extract.csv','a') as csv_file:
    writer=csv.writer(csv_file)
    writer.writerow([sign_in_text,trouble_sign_in_text,datetime.now()])
