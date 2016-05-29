__author__ = 'djfigs1'
from pyPackTF import JSONRequester

class CommunityPrices:
    json = None

    def __init__(self, key):
        self.key = key
        self.refreshPrices()

    def refreshPrices(self):
        #Note, it seems that with the Backpack.TF API you can only send a request every five minutes or so.
        url = "http://backpack.tf/api/IGetPrices/v4/?key=" + self.key
        self.json = JSONRequester.requestJSON(url)

    #Price Functions
    def isResponseSuccessful(self):
        success = self.json['response']['success']
        if success == 1:
            return True
        else:
            return False


    def getMessage(self):
        message = self.json['response']['message']
        return message

    def getCurrentTime(self):
        current_time = self.json['response']['current_time']
        return current_time
