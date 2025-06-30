from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from sigleton import singleton

class Data:
    def __init__(self, id, username, headImg):
        self.id = id
        self.username = username
        self.headImg = headImg
        
    def getId(self):
        return self.id
    
    def getUserName(self):
        return self.username
    
    def getHeadImg(self):
        return self.headImg
    
    def setId(self, id):
        self.id = id
        
    def setUserName(self, userName):
        self.username = userName
    
    def setHeadImg(self, headImg):
        self.headImg = headImg        

@singleton
class DataMgr(QObject):
    def __init__(self):
        super().__init__()
        self.datas = []
        self.id = -1
    
    def setId(self, id):
        self.id = id    
    def getId(self):
        return self.id
    
    
    def addData(self, data):
        self.datas.append(data)
        
    def addDataByINH(self, id, username, headImg):
         data = Data(id, username, headImg)
         self.addData(data)
        
    def removeDataById(self, id):
        for data in self.datas:
            if data.id == id:
                self.datas.remove(data)
                break
    def removeDataByName(self, username):
        for data in self.datas:
            if data.username == username:
                self.datas.remove(data)
                break
            
    def replaceDataById(self, id, data):
        for i in range(len(self.datas)):
            if self.datas[i].id == id:
                self.datas[i] = data
                break
            
    def replaceDataByName(self, username, data):
        for i in range(len(self.datas)):
            if self.datas[i].username == username:
                self.datas[i] = data
                break
            
    def getDataById(self, id):
        for i in range(len(self.datas)):
            if self.datas[i].id == id:
                return self.datas[i]
        return None
    
    def getDataByName(self, username):
        for i in range(len(self.datas)):
            if self.datas[i].username == username:
                return self.datas[i]
        return None
    
    def getIdByName(self, username):
        data = self.getDataByName(username)
        if data != None:
            return data.id
        return -1
    
    def getNameById(self, id):
        data = self.getDataById(id)
        if data != None:
            return data.username
        return ""