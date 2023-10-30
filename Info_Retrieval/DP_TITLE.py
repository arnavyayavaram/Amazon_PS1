import requests
from bs4 import BeautifulSoup
import csv

fields = ['ID','Title','Brand','Model']

# csvfile = open("1complete.csv", 'a',newline='',encoding="utf-8")

# csvwriter = csv.writer(csvfile)

# csvwriter.writerow(fields)

id=1
ctr=0

x=None

for j in range(1,2):

    url = 'https://www.dpreview.com/products/cameras/all?page='
    url+=str(j)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    cont=soup.find("div",class_='activeProducts')

    c=cont.find_all("div",class_='name')

    for i in c:
        help=i.find("a")
        s=""
        url=help['href']
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        paras=soup.find_all("p",_class="")

        for p in paras:
            if p.a is x:
                s+=p.text +' '


        if "Sorry" in s:
            s=""

        # print(s)

        column_title = s

        if "Manufacturer description:" == column_title[:25]:
            column_title = column_title[25:]

        if column_title == "":
            ctr+=1

        namey=soup.find("h1",_class="headerContainer")
        print(namey)

        tabrow = [id,str(column_title).strip()]
        # csvwriter.writerow(tabrow)
        # print(tabrow)

        id+=1

print(ctr)