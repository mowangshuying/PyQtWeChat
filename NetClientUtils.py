from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtNetwork import *
from PyQt6.QtWebSockets import *

from Msg import *
import time
import random
import json
import threading
from sigleton import singleton


class NetEventCaller:
    def __init__(self):
        self.call = None
        # 获取当前时间
        self.sendTime = time.time()
        self.rand = ""
        self.cmd = ""

@singleton
class NetClientUtils(QObject):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.callers = []

        self.websock = QWebSocket()
        self.websock.connected.connect(self.onConnected)
        self.websock.disconnected.connect(self.onDisconnected)
        self.websock.textMessageReceived.connect(self.onTextMessageReceived)

        # 连接远端服务器
        self.websock.open(QUrl("ws://127.0.0.1:5000"))

    def register(self, cmd, call):
        caller = NetEventCaller()
        caller.call = call
        caller.cmd = cmd
        caller.rand = ""
        self.callers.append(caller)
        

        
    # 定义回调函数，websocket连接成功时调用
    # @pyqtSlot()
    def onConnected(self):
        print("websocket connected")

    # @pyqtSlot()
    def onDisconnected(self):
        print("websocket disconnected")

    # @pyqtSlot()
    def onTextMessageReceived(self, message):
        # print("message:", message)
        data = json.loads(message)
        
        rand = data["rand"]
        msgType = data["msgType"]
        cmd = data["cmd"]
        
        for callers in self.callers:
            if callers.rand == rand and callers.cmd == cmd:
                callers.call(data)
                
                # 判断rand是否为空
                if rand != "":
                    self.callers.remove(callers)
        

    def getRandString(self):
        chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e',
        'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',]

        buf = ""
        # 生成随机数，大小在 chars 的长度内, 并设置随机种子为当前时间
        random.seed(time.time())
        for i in range(8):
            num = random.randint(0, len(chars) - 1)
            buf += chars[num]
        return buf
    
    def send(self, message):
        if self.websock.state() == QAbstractSocket.SocketState.ConnectedState:
            nLen = self.websock.sendTextMessage(message)
            return nLen > 0
        else:
            print("WebSocket is not connected.")
            return False


    def translate(self, obj):
        message = json.dumps(obj)
        return self.send(message)
        
    
    def request(self, cmd, data):
        msg = {}
        msg["cmd"] = cmd
        msg["msgType"] = MsgType.request
        msg["rand"] = ""
        msg["timestamp"] = time.time()
        msg["data"] = data
        return self.translate(msg)
        
    def request(self, cmd, data, call):
        msg = {}
        msg["cmd"] = cmd
        msg["msgType"] = MsgType.request
        msg["rand"] = self.getRandString()
        msg["timestamp"] = time.time()
        msg["data"] = data
        
        suc = self.translate(msg)
        if (suc):
            caller = NetEventCaller()
            caller.call = call
            caller.cmd = cmd
            caller.rand = msg["rand"]
            self.callers.append(caller)
            
        return suc
    
# __netClientUtils = NetClientUtils()