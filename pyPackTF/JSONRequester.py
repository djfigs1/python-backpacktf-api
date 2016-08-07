import urllib, json

def requestJSON(url):
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')

    valid = True
    retrieved_json = None
    try:
        page = urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        valid = False
        try:
            retrieved_json = json.loads(e.fp.read())
        except:
            retrieved_json = []

    if valid:
        content = page.read().decode('utf-8')
        j = json.loads(content)
        retrieved_json = j

    return retrieved_json