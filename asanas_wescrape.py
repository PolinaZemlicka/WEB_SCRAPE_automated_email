import requests
import bs4
import lxml

url = 'https://en.wikipedia.org/wiki/List_of_asanas'
res = requests.get(url)
soup = bs4.BeautifulSoup(res.text, "lxml")
table = soup.find("table",{"class":"wikitable sortable"})
links = table.findAll("a")
Asanas = []
for link in links:
    Asanas.append(link.get("title"))
print(Asanas)

