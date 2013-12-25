import requests
import json
def highest():
    url = "http://127.0.0.1:8000/api/v1/"
    doc = requests.get(url)
    print doc.content
def  xml():
    url = "http://127.0.0.1:8000/api/v1/"
    params = {'format':'xml'}
    print requests.get(url,params=params).content
def  schema():
    url = "http://localhost:8000/api/v1/contact/schema/"
    params = {'format':'json'}
    print requests.get(url,params=params).content
def getall():
    url = "http://localhost:8000/api/v1/contact/"
    params = {'format':'json','limit':0}
    c= requests.get(url,params=params).content
    print c
    l=json.loads(c)
    all=l["objects"]
    for one in all:
        print one
def newContact():
    url = "http://localhost:8000/api/v1/contact/"
    postdata = {"collection": "/api/v1/contact/1/",'wrt': 'w1', 'yiqi': '750'} #urllib.urlencode([('q','python')])# urllib.urlencode({'value': 'v', 'result': 'r'})
    headers = {'content-type': 'application/json'}
    r=requests.post(url,data=json.dumps(postdata), headers=headers)
    #print dir(r)
    #print r.status_code
    #print r.reason
    #print r.headers
    open("res.html","w").write(r.text)
def deleteContact():
    url = "http://localhost:8000/api/v1/contact/1/"
    headers = {'content-type': 'application/json'}
    params = {'format':'json'}
    print requests.delete(url,data=json.dumps(params), headers=headers).text 
def getContactbywtr():
    url = "http://localhost:8000/api/v1/contact/"
    params = {'format':'json',"apikey":"tetetgegegwt","wtr":"xs"}
    c=requests.get(url,params=params).content
    print c
if __name__=="__main__":
    # highest()
    # xml()
    # schema()
    # getbywtr()
    # print "getall==========================="
    # getall()
    newContact()
    #deletecollection()
    #newCollection()
    #getContact("mahongquan")
