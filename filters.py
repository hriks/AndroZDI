import requests
import json
import settings

api_key = settings.API_KEY
resource_id = settings.RESOURCE_ID
pincode = settings.PINCODE
url = settings.URL
api_key_train = settings.API_KEY1
train = settings.TRAINNO
url1 = settings.URL1
date = settings.DOJ
url2 = settings.URL2
trainr = settings.TRAINNO
traine = settings.TRAINNO1
urle = settings.URL3
src = settings.source
dest = settings.dest
datee = settings.date
quota = "GN"
clas = "SL"
urler = settings.URL4
pnr = settings.PNR


def filter_pnr(pnr):
    payload = pnr + "/apikey/" + api_key_train + "/"
    grl = urler + payload
    print grl
    resp = requests.get(grl)
    # data = json.loads(resp.content)
    # print type(data)
    # print data.keys()
    print payload
    return json.loads(resp.content)['passengers']


def filter_seat(traine, src, dest, datee, quota, clas):
    payload = traine + "/source/" + src + "/dest/" + dest
    payee = payload + "/date/" + datee + "/class/" + clas
    paid = payee + "/quota/" + quota + "/apikey/" + api_key_train + "/"
    grl = urle + paid
    print grl
    resp = requests.get(grl)
    print payload
    return json.loads(resp.content)['availability']


def filter_pincode(pincode):
    payload = {"api-key": api_key,
               "resource_id": resource_id,
               "filters[pincode]": pincode}
    resp = requests.get(url, params=payload)
    return json.loads(resp.content)['records']


def filter_status(train, date):
    payload = train + "/doj/" + date + "/apikey/" + api_key_train + "/"
    grl = url1 + payload
    print grl
    resp = requests.get(grl)
    print payload
    return json.loads(resp.content)['route']


def route_train(trainr):
    payload = trainr + "/apikey/" + api_key_train + "/"
    grl = url2 + payload
    print grl
    resp = requests.get(grl)
    print payload
    return json.loads(resp.content)['route']
