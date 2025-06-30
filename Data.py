from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from sigleton import singleton

class _User:
    def __init__(self):
        self.id = -1
        self.userid = -1
        self.username = ""
        self.nickname = ""
        self.sex = -1
        self.state = -1
        self.createdate = -1

# 问题:前面加下滑线就识别不到了?，后面加才可以?
@singleton
class Users:
    def __init__(self):
        self.userid = -1
        self.list = []

    def getId(self):
        return self.userid
    
    def setId(self, id):
        self.userid = id

    def add(self, user):
        self.list.append(user)

    def addDetail(self, id, userid, username, nickname, sex, state, createdate):
        user = _User()
        user.id = id
        user.userid = userid
        user.username = username
        user.nickname = nickname
        user.sex = sex
        user.state = state
        user.createdate = createdate
        self.add(user)

    def getIdByName(self, name):
        for user in self.list:
            if user.username == name:
                return user.id


    

class _GroupMsg:
    def __init__(self):
        self.id = -1
        self.ownerid = -1
        self.groupid = -1
        self.msgdata = ""
        self.msgtype = -1

@singleton
class GroupMsgs:
    def __init__(self):
        self.list = []
    
    def add(self, msg):
        self.list.append(msg)

    def addDetail(self, id, ownerid, groupid, msgdata, msgtype):
        msg = _GroupMsg()
        msg.id = id
        msg.ownerid = ownerid
        msg.groupid = groupid
        msg.msgdata = msgdata
        msg.msgtype = msgtype
        self.add(msg) 

class _GroupFriend:
    def __init__(self):
        self.id = -1
        self.ownerid = -1
        self.groupid = -1
        self.remarks = ""
        self.identify = -1

@singleton
class GroupFriends:
    def __init__(self):
        self.list = []
    
    def add(self, groupFriend):
        self.list.append(groupFriend)

    def addDetail(self, id, ownerid, groupid, remarks, identify):
        groupFriend = _GroupFriend()
        groupFriend.id = groupFriend.id
        groupFriend.ownerid = groupFriend.ownerid
        groupFriend.groupid = groupFriend.groupid
        groupFriend.remarks = groupFriend.remarks
        groupFriend.identify = groupFriend.identify
        self.add(groupFriend)
        

class _Friend:
    def __init__(self):
        self.id = -1
        self.ownerid = -1
        self.friendid = -1


@singleton
class Friends:
    def __init__(self):
        self.list = []

    def add(self, friend):
        self.list.append(friend)

    def addDetail(self, id, ownerid, friendid):
        friend = _Friend()
        friend.id = id
        friendid.ownerid = ownerid
        friendid.friendid = friendid

class _FriendMsg:
    def __init__(self):
        self.id = -1
        self.ownerid = -1
        self.friendid = -1
        self.msgdata = ""
        self.msgtype = -1

@singleton
class FriendMsgs:
    def __init__(self):
        self.list = []

    def add(self, friend):
        self.list.append(friend)

    def addDetails(self, id, ownerid, friendid, msgdata, msgtype):
        friend = _FriendMsg()
        friend.id = id
        friend.ownerid = ownerid
        friend.friendid = friendid
        friend.msgdata = msgdata
        friend.msgtype = msgtype
        self.add(friend)


class _FriendApply:
    def __init__(self):
        self.id = -1
        self.ownerid = 1
        self.friendid = -1
        self.applystate = -1
        self.applymsg = ""

@singleton
class FriendApplys:
    def __init__(self):
        self.list = []
    
    def add(self, friend):
        self.list.append(friend)

    def addDetail(self, id, ownerid, friendid, applystate, applymsg):
        apply = _FriendApply()
        apply.id = id
        apply.ownerid = ownerid
        apply.friendid = friendid
        apply.applystate = applystate
        apply.applymsg = applymsg
        self.add(apply)