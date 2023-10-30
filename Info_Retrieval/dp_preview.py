import requests
from bs4 import BeautifulSoup
import csv

t=[]
y=1

fields = ['Product_ID','Brand and Model']

csvfile = open("csvop.csv", 'a',newline='')

csvwriter = csv.writer(csvfile)

csvwriter.writerow(fields)

for i in range(1,52):

    url = 'https://www.dpreview.com/products/cameras/all?page='
    url+=str(i)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    cont=soup.find("div",class_='activeProducts')

    c=cont.find_all("div",class_='name')

    for x in c:
        t=[y,x.a.text]
        csvwriter.writerow(t)
        y+=1