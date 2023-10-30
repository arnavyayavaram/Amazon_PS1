import requests
from bs4 import BeautifulSoup

url = 'https://www.dpreview.com/products/cameras/all?page=1'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

links=[]

cont=soup.find("div",class_='activeProducts')

c=cont.find_all("div",class_='name')

for x in c:
    links.append(x.a['href'])


for link in links:

    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser')

    d=''

    paras=soup.find_all("p")

    for p in paras:
        d+=p.text +'\n'
    
    print(d)

    # table = soup.find("table",class_="")

    # rows = table.find_all("tr")

    # s=''

    # for row in rows:
    #     columns = row.find_all("td")
    #     s+=columns[0].text.strip()+' '

    # t=s+'\n'+d

    # print(t)
    print('_________________________________________________________________________________________\n')