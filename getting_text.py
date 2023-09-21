import requests
from bs4 import BeautifulSoup

url = 'https://www.digicamdb.com/cameras/'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

d=[]

for x in c:
    d.append(x.a['href'])

url = 'https://www.dpreview.com/products/fujifilm/slrs/fujifilm_xs20'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

d=''

cont=soup.find_all("p")

for c in cont:
    d+=c.text +'\n'

table = soup.find("table",class_="")

rows = table.find_all("tr")

s=''

for row in rows:
    columns = row.find_all("td")
    s+=columns[0].text.strip()+' '

t=s+'\n'+d

print(t)