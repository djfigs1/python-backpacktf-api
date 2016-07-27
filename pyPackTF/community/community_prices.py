__author__ = 'djfigs1'
from pyPackTF import JSONRequester, Exceptions

class CommunityPrices:
    classJSON = None

    def __init__(self, key, appid="440", offline=False):
        self.key = key
        self.appid = appid

        if not offline:
            self.refreshPrices()

    def refreshPrices(self, since=None):
        #Note, it seems that with the Backpack.TF API you can only send a request every five minutes or so.
        url = "http://backpack.tf/api/IGetPrices/v4/?key=" + self.key + "&appid=" + self.appid
        if since != None:
            url += "&since=" + since

        self.classJSON = JSONRequester.requestJSON(url)

        if not self.isResponseSuccessful():
            raise Exceptions.RequestFailure(self.getMessage())

    def loadJSON(self, json):
        self.classJSON = json

    #Price Functions
    def isResponseSuccessful(self):
        success = self.classJSON['response']['success']
        if success == 1:
            return True
        else:
            return False

    def getMessage(self):
        try:
            message = self.classJSON['response']['message']
        except KeyError:
            raise(Exceptions.NoErrorMessage)
        return str(message)

    def getCurrentTime(self):
        current_time = self.classJSON['response']['current_time']
        return current_time

    def getCommunityItems(self):
        communityItems = []
        for item, keys in self.classJSON['response']['items'].items():
            communityItems.append(CommunityItem(item, keys))

        return communityItems

class CommunityItem:
    def __init__(self, item, itemJSON):
        self.itemJSON = itemJSON
        self.item = item

    def getName(self):
        return self.item

    def getDefIndexes(self):
        return self.itemJSON['defindex']

    def getQualities(self):
        return_qualities = []
        for item, keys in self.itemJSON['prices'].items():
            return_qualities.append(item)

        return return_qualities

    def getPrice(self, quality, tradable=True, craftable=True, priceIndex=0):
        if (tradable):
            str_tradable = "Tradable"
        else:
            str_tradable = "Untradable"
        if (craftable):
            str_craftable = "Craftable"
        else:
            str_craftable = "Uncraftable"
        return self.itemJSON['prices'][str(quality)][str_tradable][str_craftable][priceIndex]['value']

    def getCurrency(self, quality, tradable=True, craftable=True, priceIndex=0):
        if (tradable):
            str_tradable = "Tradable"
        else:
            str_tradable = "Untradable"
        if (craftable):
            str_craftable = "Craftable"
        else:
            str_craftable = "Uncraftable"

        return self.itemJSON['prices'][str(quality)][str_tradable][str_craftable][priceIndex]['currency']


    def getDifference(self, quality, tradable=True, craftable=True, priceIndex=0):
        if (tradable):
            str_tradable = "Tradable"
        else:
            str_tradable = "Untradable"
        if (craftable):
            str_craftable = "Craftable"
        else:
            str_craftable = "Uncraftable"

        return self.itemJSON['prices'][str(quality)][str_tradable][str_craftable][priceIndex]['difference']

    def getLastUpdated(self, quality, tradable=True, craftable=True, priceIndex=0):
        if (tradable):
            str_tradable = "Tradable"
        else:
            str_tradable = "Untradable"
        if (craftable):
            str_craftable = "Craftable"
        else:
            str_craftable = "Uncraftable"

        return self.itemJSON['prices'][str(quality)][str_tradable][str_craftable][priceIndex]['last_update']