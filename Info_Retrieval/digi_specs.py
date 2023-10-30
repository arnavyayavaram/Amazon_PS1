import requests
from bs4 import BeautifulSoup
import csv
import math

fields = ['Product_ID','Specs']
csvfile = open("spec2.csv", 'a',newline='',encoding="utf-8")
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

        table = soup.find("table",class_="w100 table_specs font_smaller")

        rows = table.find_all("tr")

        for row in rows:
            column_name = row.find("td",class_='right')
            column_value = row.find("td",class_='')

            tabrow = [id,str(column_name.text).strip(),str(column_value.text).strip()]
            csvwriter.writerow(tabrow)
        id+=1

    for i in range(2,bread+1):
        response = requests.get(url+v+str(i)+"/")
        soup = BeautifulSoup(response.content, 'html.parser')

        f=soup.find_all('div',class_='newest_2')

        for p in f:
            response = requests.get(spec+p.a['href'])
            soup = BeautifulSoup(response.content, 'html.parser')

            table = soup.find("table",class_="w100 table_specs font_smaller")

            rows = table.find_all("tr")

            for row in rows:
                column_name = row.find("td",class_='right')
                column_value = row.find("td",class_='')

                tabrow = [id,str(column_name.text).strip(),str(column_value.text).strip()]
                csvwriter.writerow(tabrow)
            id+=1