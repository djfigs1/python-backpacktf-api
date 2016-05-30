__author__ = 'djfigs1'
from pyPackTF import JSONRequester

class MarketItem:
    json = None

    def __init__(self, item, itemJSON):
        self.json = itemJSON
        self.item = item

    def getName(self):
        return self.item

    def getLastUpdated(self):
        return self.json['last_updated']

    def getQuantity(self):
        return self.json['quantity']

    def getValue(self):
        return self.json['value']

    def getFormatedValue(self):
        value = float(self.json['value'])
        return value / 100

class MarketPrices:
    #Default App ID for Market Prices is 440, which is TF2.

    def __init__(self, key, appid=440):
        self.key = key
        self.id = appid
        self.requestMarketPrices()

    def requestMarketPrices(self):
        #You can only send requests every sixty seconds.
        url = "http://backpack.tf/api/IGetMarketPrices/v1/?key=" + self.key + "&appid=" + str(self.id)
        self.json = JSONRequester.requestJSON(url)

    #Response Functions
    def isResponseSuccessful(self):
        success = self.json['response']['success']
        if success == 1:
            return True
        else:
            return False

    def getFailureMessage(self):
        #Only use this if isResponseSuccessful is 0
        try:
            message = self.json['response']['message']
        except KeyError:
            message = ""
        return str(message)

    def getServerTime(self):
        time = self.json['response']['current_time']
        return time

    def getMarketItems(self):
        j = self.json
        items = j['response']['items'].items()
        marketItems = []

        for item, keys in items:
            marketItems.append(MarketItem(item, keys))

        return marketItems
