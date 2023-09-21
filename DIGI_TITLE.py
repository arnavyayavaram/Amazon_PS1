import requests
from bs4 import BeautifulSoup
import csv
import math

fields = ['Product_ID','Specs']
csvfile = open("desc2.csv", 'a',newline='',encoding="utf-8")
csvwriter = csv.writer(csvfile)
csvwriter.writerow(fields)

url = 'https://www.digicamdb.com/cameras/'
spec='https://www.digicamdb.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

c=soup.find_all('div',class_='font_tiny')

id=1

for x in c:
    b=int(x.find_all('b')[1].text)
    a=x.a['href']

    # print(a,b)

    v=a[7:]

    bread=math.ceil(b/25)

    response = requests.get(url+v)
    soup = BeautifulSoup(response.content, 'html.parser')

    f=soup.find_all('div',class_='newest_2')

    for p in f:
        response = requests.get(spec+p.a['href'])
        soup = BeautifulSoup(response.content, 'html.parser')

        desc = soup.find("div",class_="font_smaller pad")

        tabrow=[id,(desc.text.replace("\n",""))]
        csvwriter.writerow(tabrow)
        id+=1

    for i in range(2,bread+1):
        response = requests.get(url+v+str(i)+"/")
        soup = BeautifulSoup(response.content, 'html.parser')

        f=soup.find_all('div',class_='newest_2')

        for p in f:
            response = requests.get(spec+p.a['href'])
            soup = BeautifulSoup(response.content, 'html.parser')
            desc = soup.find("div",class_="font_smaller pad")

            tabrow=[id,(desc.text.replace("\n",""))]
            csvwriter.writerow(tabrow)
            id+=1