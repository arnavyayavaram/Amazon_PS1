import requests
from bs4 import BeautifulSoup
import csv
import math

fields = ['Product_ID','Brand and Model']
csvfile = open("csvop2.csv", 'a',newline='')
csvwriter = csv.writer(csvfile)
csvwriter.writerow(fields)

url = 'https://www.digicamdb.com/cameras/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

c=soup.find_all('div',class_='font_tiny')

ctr=1

for x in c:
    b=int(x.find_all('b')[1].text)
    a=x.a['href']

    bread=math.ceil(b/25)

    v=a[7:]

    response = requests.get(url+v)
    soup = BeautifulSoup(response.content, 'html.parser')

    f=soup.find_all('div',class_='newest_2')

    for p in f:
        csvwriter.writerow([ctr,p.b.a.text.strip()])
        ctr+=1

    for i in range(2,bread+1):
        response = requests.get(url+v+str(i)+"/")
        soup = BeautifulSoup(response.content, 'html.parser')

        f=soup.find_all('div',class_='newest_2')

        for p in f:
            csvwriter.writerow([ctr,p.b.a.text.strip()])
            ctr+=1