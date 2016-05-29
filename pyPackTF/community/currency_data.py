__author__ = 'djfigs1'
from pyPackTF import JSONRequester

class CurrencyData:
    json = None

    def __init__(self, key):
        self.key = key
        self.refreshPrices()


    def refreshPrices(self):
        #Note, it seems that with the Backpack.TF API you can only send a request every five minutes or so.
        url = "http://backpack.tf/api/IGetCurrencies/v1/?key=" + self.key
        self.json = JSONRequester.requestJSON(url)


    #Response Functions
    def isResponseSuccessful(self):
        success = self.json['response']['success']
        if success == 1:
            return True
        else:
            return False

    def getFailureMessage(self):
        try:
            message = self.json['response']['message']
        except KeyError:
            message = ""
        return message

    def getCurrentTime(self):
        time = self.json['response']['current_time']
        return time

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

