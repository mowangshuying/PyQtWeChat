class MsgType:
    # def __init__(self):
        request = "request"
        response = "response"
        requestS = "requestS"
        responseS = "responseS"
        push = "push"
        broadcast = "broadcast"
        pushS = "pushS"

class MsgState:
    # def __init__(self):
        ok = "ok"
        error = "error"
        timeout = "timeout"
        notFound = "notFound"
        serverBusy = "serverBusy"
        serverOffline = "serverOffline"



class MsgCmd:
    # def __init__(self):
        login = "login"
        logout = "logout"
        regUser = "regUser"
        changePassword = "changePassword"
        sendMsg = "sendMsg"
        sendGroupMsg = "sendGroupMsg"
        updateSessionList = "updateSessionList"
        updateGroupList = "updateGroupList"
        updateFriendList = "updateFriendList"
        applyAddUser = "applyAddUser"
        createGroup = "createGroup"
        doApplyAddUser = "doApplyAddUser"
        getApplyFriendList = "getApplyFriendList"
        findUser = "findUser"
        setGroupName = "setGroupName"
        getFriendList = "getFriendList"
        getSessionList = "getSessionList"
        getGroupList = "getGroupList"
        updateHeadImg = "updateHeadImg"
        getGroupInfo = "getGroupInfo"
        callPhone = "callPhone"
        acceptPhone = "acceptPhone"
        closePhone = "closePhone"