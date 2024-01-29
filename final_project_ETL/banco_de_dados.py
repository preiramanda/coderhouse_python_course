import sqlite3

conn = sqlite3.connect('dados_api.db')
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS country1 (id INTEGER PRIMARY KEY AUTOINCREMENT, pais VARCHAR(100) NOT NULL, regiao VARCHAR(200) NOT NULL, mapa VARCHAR (500) NOT NULL)')
cursor.execute('CREATE TABLE IF NOT EXISTS country2 (id INTEGER PRIMARY KEY AUTOINCREMENT, pais VARCHAR(100) NOT NULL, regiao VARCHAR(200) NOT NULL, mapa VARCHAR (500) NOT NULL)')
cursor.execute('CREATE TABLE IF NOT EXISTS country3 (id INTEGER PRIMARY KEY AUTOINCREMENT, pais VARCHAR(100) NOT NULL, regiao VARCHAR(200) NOT NULL, mapa VARCHAR (500) NOT NULL)')

conn.commit
conn.close