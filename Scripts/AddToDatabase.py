#!/usr/bin/python3

import sqlite3, os

def AddToDB():
    print(os.path.isfile('database.db'))
    if os.path.isfile('database.db'):
        db = sqlite3.connect('database.db')
        
    else:
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE movies(id INTEGER primary key,
        title TEXT, director TEXT, cast TEXT, writers TEXT, runtime TEXT
        rated TEXT, year TEXT, genre TEXT, awards TEXT, imdb REAL,
        tomoto REAL, plot TEXT, poster TEXT, hash TEXT)''')
        db.commit()
