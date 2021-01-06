import requests
import bs4
import lxml
import sqlite3

url = 'https://en.wikipedia.org/wiki/List_of_asanas'
res = requests.get(url)
soup = bs4.BeautifulSoup(res.text, "lxml")
table = soup.find("table",{"class":"wikitable sortable"})

# empty lists of:
Asanas = []
English = []

# iterate over html
for row in table.findAll("tr"):
    cells=row.findAll("td")
    if len(cells) == 9:
        Asanas.append(cells[0].find(text=True))
        English.append(cells[2].find(text=True).replace("\n","").replace(",",""))

print(Asanas)
print(English)


# # create a database & connect
# connection = sqlite3.connect("asanas.db")
# # cursor
# crsr = connection.cursor()

# comment out what is already executed:
# SQL command to create a table in the database
# sql_command = """CREATE TABLE asanas (
# ID INTEGER PRIMARY KEY AUTOINCREMENT,
# name VARCHAR(50),
# english VARCHAR(50),
# Image BLOB);"""

# execute the statement

# crsr.execute(sql_command)

# crsr.executemany("INSERT INTO asanas(name, english) VALUES(?,?)",
#                  zip(Asanas, English))
# connection.commit()

