__author__ = 'djfigs1'
import urllib2,json

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
        value = int(self.json['value'])
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
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
        req = urllib2.Request(url, headers=hdr)

        valid = True
        try:
            page = urllib2.urlopen(req)
        except urllib2.HTTPError, e:
            valid = False
            self.json = json.loads(e.fp.read())

        if valid:
            content = page.read()
            j = json.loads(content)
            self.json = j

    #Response Functions
    def isResponseSuccessful(self):
        success = self.json['response']['success']
        if success == 1:
            return True
        else:
            return False

    def getFailureMessage(self):
        #Only use this if isResponseSuccessful is 0
        message = self.json['response']['message']
        return str(message)

    def getCurrentTime(self):
        time = self.json['response']['current_time']
        return time

    def getMarketItems(self):
        j = self.json
        items = j['response']['items'].items()
        marketItems = []

        for item, keys in items:
            marketItems.append(MarketItem(item, keys))

        return marketItems
