#!/usr/bin/python3

# Hashes the video files and gathers data
# from OpenSubtitles and OMDBAPI
from .HashGenerator import HashFile
from .GetOpenSubtitlesData import GetToken, RequestImdbID
from .GetOmdbApiData import GetMovieData
from .DatabaseOperations import AddToDB, ArrangeData
import os, sqlite3, re

def GetData(ListOfMovies):
    try:
        p = re.compile('sample')
        token = GetToken()
        for i in ListOfMovies:
            if not(p.search(i.lower())):
                ImdbID = None
                HashOfFile = HashFile(i)
                if(HashOfFile != 'SizeError'):
                    if(os.path.isfile('database.db')):
                        db = sqlite3.connect('database.db')
                        cursor = db.cursor()
                        cursor.execute('SELECT * FROM movies WHERE hash = ?', (HashOfFile,))
                        if(len(cursor.fetchall())==0):
                            ImdbID = RequestImdbID(token, HashOfFile)
                        else:
                            continue
                        db.close()
                    else:
                        ImdbID = RequestImdbID(token, HashOfFile)
                else:
                    pass
                
                if(ImdbID != None):
                    MovieData = GetMovieData(ImdbID)
                    ArrangedData = ArrangeData((MovieData, HashOfFile, i))
                    AddToDB(ArrangedData)
                    
            else:
                pass
     
    except(AttributeError):
       pass
    
    except(socket.gaierror):
        
            
