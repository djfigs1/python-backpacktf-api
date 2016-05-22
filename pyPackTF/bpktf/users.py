__author__ = 'djfigs1'
import urllib2,json

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

def requestSteamIDS(steamids):
    ids = ""
    nomOfIDS = len(steamids)

    x = 1
    for steamid in steamids:
        ids = ids + steamid
        if x < nomOfIDS:
            ids = ids + ","
        x = x + 1

    url = "http://backpack.tf/api/IGetUsers/v3/?steamids=" + ids

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

    return j

def getBPKUsers(steamids):
    j = requestSteamIDS(steamids)
    ids = j['response']['players'].items()
    BPKUsers = []

    for item, keys in ids:
        BPKUsers.append(BPKUser(keys))

    return BPKUsers




