from enum import Enum

class ChatRole(Enum):
    Self = 1
    Other = 2
    
class SesType(Enum):
    Friend = 1
    Group = 2