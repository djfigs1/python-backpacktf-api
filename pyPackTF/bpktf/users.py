__author__ = 'djfigs1'
from pyPackTF import JSONRequester
class BPKUser:
    def __init__(self, userJson):
        self.userJson = userJson

    def getSuccess(self):
        return self.userJson['success']

    def getSteamID(self):
        return self.userJson['steamid']

    def getName(self):
        return self.userJson['name']

    def getBackpackValue(self, id):
        return self.userJson['backpack_value'][id]

    def getBackpackUpdate(self, id):
        return self.userJson['backpack_update'][id]

    def getBackpackTFBanned(self):
        return self.userJson['backpack_tf_banned']

    def getBackpackTFReputation(self):
        return self.userJson['backpack_tf_reputation']

    def getBackpackTFGroup(self):
        return self.userJson['backpack_tf_group']

    def getBackpackTFPosititveTrust(self):
        return self.userJson['backpack_tf_trust']['for']

    def getBackpackTFNegativeTrust(self):
        return self.userJson['backpack_tf_trust']['against']

    def getSteamRepScammer(self):
        return self.userJson['steamrep_scammer']

    def getBanEconomy(self):
        return self.userJson['ban_economy']

    def getBanCommunity(self):
        return self.userJson['ban_community']

    def getBanVAC(self):
        return self.userJson['ban_vac']

class UserRequester:
    def requestSteamIDS(self, steamids):
        ids = ""
        nomOfIDS = len(steamids)

        x = 1
        for steamid in steamids:
            ids = ids + steamid
            if x < nomOfIDS:
                ids = ids + ","
            x = x + 1

        url = "http://backpack.tf/api/IGetUsers/v3/?steamids=" + ids
        j = JSONRequester.requestJSON(url)

        return j

    def getBPKUsers(self, steamids, json=None):
        #Say you only want to get one user and you enter in a string, this will make it compatible with the requestSteamIDS function.
        if json == None:
            if isinstance(steamids, basestring):
                steamids = [steamids]

            j = self.requestSteamIDS(steamids)
        else:
            j = json

        ids = j['response']['players'].items()
        BPKUsers = []

        for item, keys in ids:
            BPKUsers.append(BPKUser(keys))

        return BPKUsers






