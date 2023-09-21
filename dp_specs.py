import requests
from bs4 import BeautifulSoup
import csv

d=[]

fields = ['ID','Attribute','Value']

csvfile = open("camspecs.csv", 'a',newline='',encoding="utf-8")

csvwriter = csv.writer(csvfile)

csvwriter.writerow(fields)

for i in range(1,52):

    url = 'https://www.dpreview.com/products/cameras/all?page='
    url+=str(i)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    cont=soup.find("div",class_='activeProducts')

    c=cont.find_all("div",class_='name')

    for i in c:
        help=i.find("a")
        d.append(help['href'])
        # print(help['href'])


id=1

x=None

for link in d:

    url=link
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find("table",class_="")

    rows = table.find_all("tr")

    # print(rows)

    for row in rows:
        column_name = row.find("th")
        column_value = row.find("td")
        if(column_name is x):
            continue
        tabrow = [id,str(column_name.text).strip(),str(column_value.text).strip()]
        # print(tabrow)
        csvwriter.writerow(tabrow)
    id+=1

    


