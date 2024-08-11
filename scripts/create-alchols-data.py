import sqlite3
import requests
import json

# APIをたたいてアルコールのリスト作成
url = "https://muro.sakenowa.com/sakenowa-data/api/brands"
responce = requests.get(url)
data = responce.json()
brands = data['brands']

conn = sqlite3.connect('test.db')
cursor = conn.cursor();

def create_alcohol_data(id, name):
# SQLiteにデータ保存


  cursor.execute('''
  INSERT INTO alcohol (id, name) VALUES(?, ?)
  ''', (id, name))

for i in range(0,9):
  create_alcohol_data(i,brands[i]['name'])

conn.commit()
conn.close()

print("data")



