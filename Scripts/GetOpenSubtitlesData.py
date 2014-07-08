#	The GetOpenSubtitlesData module implements 2 functions.
#	GetToken() returns a token required for further queries
#	RequestImdbID() returns the IMDB id retrieved from OpenSubtitles

import xmlrpc.client

def GetToken():
    try:
        server = xmlrpc.client.ServerProxy("http://api.opensubtitles.org/xml-rpc")
        TokenData = server.LogIn('','','','OS Test User Agent')
                
        return TokenData['token']
                
    except(ConnectionError):
        pass

                
def RequestImdbID(token, hash):
    try:
        server = xmlrpc.client.ServerProxy("http://api.opensubtitles.org/xml-rpc")
        IdData = server.CheckMovieHash2(token,[hash])
        if(len(IdData['data']) != 0):
            if(IdData['data'][hash][0]['MovieKind'] == 'movie'):        
                return 'tt'+IdData['data'][hash][0]['MovieImdbID']
            else:
                pass
        else:
            pass
                
    except(ConnectionError):
        pass
