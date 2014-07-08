# Import the os module, for the os.walk function
import os
from PyQt4 import QtCore, QtGui

MovieExtensions = ['avi', 'dat', 'mp4', 'mkv', 'vob']

def GetDirectoryForVideos():
    try:
        path = QtGui.QFileDialog.getExistingDirectory()
        return GetListOfVideos(path)
        
    except(AttributeError):
        pass
        
def GetPathForVideo():
    try:
        MovieList = []
        path = QtGui.QFileDialog.getOpenFileName()
        MovieList.append(path)
        
        return MovieList
        
    except(AttributeError):
        pass
        
def GetListOfVideos(path):
    try:
        MovieList = []
        for dirName, subdirList, fileList in os.walk(path):
            for fname in fileList:
                if fname[-3:] in MovieExtensions:
                    MovieList.append(os.path.join(dirName,fname))
        
        return MovieList

    except(IOError):
        pass
