#	The GetOmdbApiData module uses the IMDB movie ID to get information about a movie
#	from http://www.omdbapi.com/


import urllib.request

def GetMovieData(id):
    try:
        OmdbApiUrl = 'http://www.omdbapi.com/?i='
        MovieUrl = OmdbApiUrl+id+'&plot=full&tomatoes=true'
        MovieData = eval(urllib.request.urlopen(MovieUrl).read().decode())
                
        return MovieData
        
    except(urllib.error.URLError):
        pass
        
