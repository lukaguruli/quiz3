import requests
import json
import sqlite3
url = "https://color.serialif.com/aquamarine"

quiz = requests.get(url)

print(quiz.status_code)
print(quiz.headers)
print(quiz.text)

quiz2 = quiz.json()

with open('aquamarine.json','w') as aquamarine:
    json.dump(quiz2,aquamarine,indent=4)



for k in quiz2:
    print(quiz2[k]["value"]+", " + k["lightness"])


c = sqlite3.connect('lukino.sqlite')
cursor = c.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS aquamarine
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                value VARCHAR(50),
                lightness VARCHAR(255),
                saturation INTEGER
''')

list = []

for e in quiz2:
    value = quiz2[e]["value"]
    lightness = quiz2[e]["lightness"]
    list2 = [value,lightness]
    list.append(list2)

cursor.executemany('''INSERT INTO aquamarine (value ,lightness,saturation)
                       VALUES (?,?,?)''',list)

c.commit()
c.close()


