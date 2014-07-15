#!/usr/bin/python3

from PyQt4 import QtCore, QtGui
import UiFiles.Ui_MainWindow
from Scripts import GetListOfVideos, GetDataFromWeb, DatabaseOperations
import sys, os

class pmm(QtGui.QMainWindow):
    def __init__(self, parent = None):
        super(pmm, self).__init__(parent)
        self.ui = UiFiles.Ui_MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.connect(self.ui.addFolder, QtCore.SIGNAL("clicked()"), self.addFolder)
        self.connect(self.ui.addMovie, QtCore.SIGNAL("clicked()"), self.addMovie)
        self.connect(self.ui.remove, QtCore.SIGNAL("clicked()"), self.remove)
        self.connect(self.ui.play, QtCore.SIGNAL("clicked()"), self.play)
        self.connect(self.ui.save, QtCore.SIGNAL("clicked()"), self.save)
        self.connect(self.ui.info, QtCore.SIGNAL("clicked()"), self.info)
        self.connect(self.ui.listWidget, QtCore.SIGNAL("itemSelectionChanged()"), self.updateDisplay)
        
        self.reloadList()
        
    def addFolder(self):
        GetDataFromWeb.GetData(GetListOfVideos.GetDirectoryForVideos())
        self.reloadList()
        
    def addMovie(self):
        GetDataFromWeb.GetData(GetListOfVideos.GetPathForVideo())
        self.reloadList()
    
    def updateDisplay(self):
        try:
            self.values = DatabaseOperations.UpdateDisplay(self.ui.listWidget.currentItem().text())
            self.ui.title.setText(self.values[1])
            self.ui.director.setText(self.values[2])
            self.ui.cast.setText(self.values[3])
            self.ui.writers.setText(self.values[4])
            self.ui.runtime.setText(self.values[5])
            self.ui.rated.setText(self.values[6])
            self.ui.year.setText(self.values[7])
            self.ui.genre.setText(self.values[8])
            self.ui.awards.setText(self.values[9])
            self.ui.imdb.setText(self.values[10])
            self.ui.tomato.setText(self.values[11])
            self.ui.plot.setText(self.values[12])
            if(self.values[13] != 'Poster Not Available'):
                self.ui.poster.setPixmap(QtGui.QPixmap(self.values[13]))
            else:
                self.ui.poster.setText('Poster Not Available')
            
            self.currentMovieName = self.values[1]
        
        except(TypeError):
            self.ui.title.setText('')
            self.ui.director.setText('')
            self.ui.cast.setText('')
            self.ui.writers.setText('')
            self.ui.runtime.setText('')
            self.ui.rated.setText('')
            self.ui.year.setText('')
            self.ui.genre.setText('')
            self.ui.awards.setText('')
            self.ui.imdb.setText('')
            self.ui.tomato.setText('')
            self.ui.plot.setText('')
            self.ui.poster.setText('Poster Not Available')
            
            self.currentMovieName = ''
            
    def play(self):
        try:
            DatabaseOperations.PlayMovie(self.ui.listWidget.currentItem().text())
        
        except(AttributeError):
            pass
    
    def save(self):
        
    def info(self):
        pass
        
    def remove(self):
        try:
            DatabaseOperations.RemoveMovie(self.ui.listWidget.currentItem().text())
            self.reloadList()
        
        except(AttributeError):
            pass
            
    
    def reloadList(self):
        try:
            if os.path.isfile('database.db'):
                DatabaseOperations.RemoveDeletedFiles()
                self.titles = DatabaseOperations.LoadList()
                self.ui.listWidget.clear()
                self.ui.listWidget.insertItems(0, self.titles)
            else:
                pass
        except(TypeError):
            pass
        
if __name__=='__main__':
    app=QtGui.QApplication(sys.argv)
    myapp = pmm()
    myapp.show()
    app.exec_()
