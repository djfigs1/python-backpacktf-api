__author__ = 'djfigs1'
import urllib2, json

class CurrencyData:
    json = None

    def __init__(self, key):
        self.key = key
        self.refreshPrices()


    def refreshPrices(self):
        #Note, it seems that with the Backpack.TF API you can only send a request every five minutes or so.
        url = "http://backpack.tf/api/IGetCurrencies/v1/?key=" + self.key
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

        req = urllib2.Request(url, headers=hdr)

        try:
            page = urllib2.urlopen(req)
        except urllib2.HTTPError, e:
            print e.fp.read()

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
        message = self.json['response']['message']
        return message

    def getCurrentTime(self):
        time = self.json['response']['current_time']
        return time


    # -==- Currency Functions -==-

    # --- Refined Metal ---
    def getMetalValue(self):
        value = self.json['response']['currencies']['metal']['price']['value']
        return value

    def getMetalValueHigh(self):
        value = self.json['response']['currencies']['metal']['price']['value_high']
        return value

    def getMetalValueDifference(self):
        value = self.json['response']['currencies']['metal']['price']['difference']
        return value

    def getMetalCurrency(self):
        currency = self.json['response']['currencies']['metal']['price']['currency']
        return currency

    # --- Keys ---
    def getKeyValue(self):
        value = self.json['response']['currencies']['keys']['price']['value']
        return value

    def getKeyValueHigh(self):
        value = self.json['response']['currencies']['keys']['price']['value_high']
        return value

    def getKeyValueDifference(self):
        value = self.json['response']['currencies']['keys']['price']['difference']
        return value

    def getKeyCurrency(self):
        currency = self.json['response']['currencies']['keys']['price']['currency']
        return currency

    # --- Earbuds ----
    def getEarbudsValue(self):
        value = self.json['response']['currencies']['earbuds']['price']['value']
        return value

    def getEarbudsValueHigh(self):
        value = self.json['response']['currencies']['earbuds']['price']['value_high']
        return value

    def getEarbudsValueDifference(self):
        value = self.json['response']['currencies']['earbuds']['price']['difference']
        return value

    def getEarbudsCurrency(self):
        currency = self.json['response']['currencies']['earbuds']['price']['currency']
        return currency

    # --- Hats  ---
    def getHatValue(self):
        value = self.json['response']['currencies']['hat']['price']['value']
        return value

    def getHatValueHigh(self):
        value = self.json['response']['currencies']['hat']['price']['value_high']
        return value

    def getHatValueDifference(self):
        value = self.json['response']['currencies']['hat']['price']['difference']
        return value

    def getHatCurrency(self):
        currency = self.json['response']['currencies']['hat']['price']['currency']
        return currency

