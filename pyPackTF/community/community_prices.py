__author__ = 'djfigs1'
from pyPackTF import JSONRequester

class CommunityPrices:
    classJSON = None

    def __init__(self, key, appid=440, since=None):
        self.key = key
        self.refreshPrices()
        self.appid = appid
        self.since = since

    def refreshPrices(self):
        #Note, it seems that with the Backpack.TF API you can only send a request every five minutes or so.
        url = "http://backpack.tf/api/IGetPrices/v4/?key=" + self.key
        self.classJSON = JSONRequester.requestJSON(url)

    #Price Functions
    def isResponseSuccessful(self):
        success = self.classJSON['response']['success']
        if success == 1:
            return True
        else:
            return False

    def getMessage(self):
        message = self.classJSON['response']['message']
        return message

    def getCurrentTime(self):
<<<<<<< HEAD
        current_time = self.classJSON['response']['current_time']
=======
        current_time = self.json['response']['current_time']
>>>>>>> master
        return current_time

class CommunityItem:
    def __init__(self, item, itemJSON):
        self.itemJSON = itemJSON
        self.item = item

    def getName(self):
        return self.item

    def getDefIndexes(self):
        return self.itemJSON['defindex']

