#!/usr/bin/python3

import sqlite3, os, sys, subprocess
import urllib.request

def AddToDB(data):
    try:
        if os.path.isfile('database.db'):
            db = sqlite3.connect('database.db')
            cursor = db.cursor()
            
        else:
            db = sqlite3.connect('database.db')
            cursor = db.cursor()
            cursor.execute('''CREATE TABLE movies(id INTEGER primary key,
            title TEXT, director TEXT, cast TEXT, writers TEXT, runtime TEXT,
            rated TEXT, year TEXT, genre TEXT, awards TEXT, imdb TEXT,
            tomato TEXT, plot TEXT, poster TEXT, hash TEXT, file TEXT)''')
            db.commit()
        
        cursor.execute('''INSERT INTO movies(title, director, cast, writers, 
            runtime, rated, year, genre, awards, imdb, tomato, plot, poster, 
            hash, file) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', data)
        
        print('First user inserted')
        db.commit()
        db.close()
        
    except(ValueError):
        pass

def ArrangeData(data):
    try:
        FileLocation = data[2]
        FileHash = data[1]
        ImdbData = data[0]
        
        title = ImdbData['Title']
        director = ImdbData['Director']
        cast = ImdbData['Actors']
        writers = ImdbData['Writer']
        runtime = ImdbData['Runtime']
        rated = ImdbData['Rated']
        year = ImdbData['Year']
        genre = ImdbData['Genre']
        awards = ImdbData['Awards']
        imdb = ImdbData['imdbRating']
        tomato = ImdbData['tomatoUserRating']
        plot = ImdbData['Plot']
        poster = ImdbData['Poster']
        
        try:
            urllib.request.urlretrieve(poster, os.path.join(os.getcwd(), 'Posters', poster.split('/')[-1])) #Download poster
            poster = os.path.join(os.getcwd(), 'Posters', poster.split('/')[-1]) #Set poster to link to local file
        except(ValueError):
            poster = 'Poster Not Available'
        except(FileNotFoundError):
            os.mkdir(os.path.join(os.getcwd(), 'Posters'))
            urllib.request.urlretrieve(poster, os.path.join(os.getcwd(), 'Posters', poster.split('/')[-1])) #Download poster
            poster = os.path.join(os.getcwd(), 'Posters', poster.split('/')[-1]) #Set poster to link to local file
            
        
        title = title +' ('+ year + ')'
        
        return (title, director, cast, writers, runtime, rated, year, genre, awards, imdb, tomato, plot, poster, FileHash, FileLocation)
    
    except(KeyError):
        pass
            
    
def LoadList():
    if os.path.isfile('database.db'):
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        cursor.execute('''SELECT title FROM movies''')
        titles = []
        value = cursor.fetchall()
        for i in value:
            titles.append(i[0])
        db.close()
        return titles
    
    else:
        pass


def UpdateDisplay(CurrentTitle):
    try:
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM movies WHERE title=?',(CurrentTitle,))
        value = cursor.fetchall()
        db.close()
        return value[0]
        
    except(IndexError):
        pass
    
def PlayMovie(CurrentTitle):
    try:
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        cursor.execute('SELECT file FROM movies WHERE title=?',(CurrentTitle,))
        value = cursor.fetchone()
        db.close()
        
        if sys.platform == "win32":
            os.startfile(value[0])
        else:
            opener ="open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, value[0]])
        
    except(KeyError):
        print("Error")
        
def RemoveDeletedFiles():
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.execute('SELECT file FROM movies')
    value = cursor.fetchall()
    for i in value:
        if not(os.path.isfile(i[0])):
            try:
                cursor.execute('SELECT poster FROM movies WHERE file=?',i)
                os.remove(cursor.fetchone()[0][0])
            except(IsADirectoryError):
                pass
            
            cursor.execute('DELETE FROM movies WHERE file=?',i)
        else:
            pass
    
    db.commit()
    db.close()
    
def RemoveMovie(CurrentTitle):
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    try:
        cursor.execute('SELECT poster FROM movies WHERE title=?',(CurrentTitle,))
        os.remove(cursor.fetchone()[0])
    except(IsADirectoryError):
        pass
        
    cursor.execute('DELETE FROM movies WHERE title=?',(CurrentTitle,))
    db.commit()
    db.close()
