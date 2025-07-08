from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class SyncEvent:
    def __init__(self, state = False, parent = None):
        self.state = state
        self.mutex = QMutex()
        self.cond = QWaitCondition()
        
    def set(self):
        self.mutex.lock()
        self.state = True
        self.cond.wakeAll()
        self.mutex.unlock()
        
    def clear(self):
        self.mutex.lock()
        self.state = False
        self.mutex.unlo
        
    def wait(self, timeout):
        result = False
        self.mutex.lock()
        if not self.state:
            if timeout < 0:
                self.cond.wait(self.mutex)
                result = True
            else:
                result = self.cond.wait(self.mutex, timeout)
        else:
            result = True
            
        self.mutex.unlock()
        return result
    
    def isSet(self):
        return self.state    
