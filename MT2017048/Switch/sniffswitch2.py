#!/usr/bin/python
import httplib
import sys
import time
from random import *
from scapy.all import *
from threading import Timer
import requests,json
import socket 
from uuid import getnode as get_mac
import json


stars = lambda n: "*" * n
#myObj = { "name":"John", "age":30, "car":null };
#x = myObj.name;

#contenttypes = json.loads(request.POST.get('mydata', "{}"))
contenttypes={}
count = 0
#macaddr = {}
macaddr = "00:00:00:00:00:02"
#json_macaddr = json.dumps(macaddr)


def GET_print(packet):
    url = "".join(packet.sprintf("{Raw:%Raw.load%}").split(r"\r\n"))
    content_name = url.split()
    
    extract_url(content_name)
    return "\n".join((
        stars(40) + "GET PACKET" + stars(40),
        "\n".join(packet.sprintf("{Raw:%Raw.load%}").split(r"\r\n")),
        stars(90)))

def extract_url(data):
    #p = re.compile('content*')
    if len(data) >= 0:
        #if p.match(data[1]):
        print "Url:" + data[1]
 
        if data[1] not in contenttypes:
            
            contenttypes[data[1]] = {}
            contenttypes[data[1]]["Count"] = 1
            contenttypes[data[1]]["mac"] = macaddr
        else:
            contenttypes[data[1]]["Count"] += 1
            #contenttypes[data[1]]["mac"] = macaddr
        

    print 'Content types =========================================>'
    print contenttypes
    #send_data(contenttypes)


def send_data(data):
    print "hello"
    s = socket.socket() 
    
    port = 65532 
    s.connect(('10.0.2.15', port))
    #data = json.dumps(data)
    #c = {key: value for (key, value) in (data.items() + macaddr.items())}
    c = json.dumps(contenttypes)

    #jsondata = json.loads(c)    
    stringdata = str(c)
    print 'sent ===>'
    print stringdata
    s.send(stringdata)
    print s.recv(1024)
    #contenttypes={}
    #s.close()


while True:
    t = Timer(15.0, send_data,[contenttypes])
    t.start()
    sniff(
	    prn=GET_print,
	    lfilter=lambda p: "GET" in str(p),
	    filter="tcp port 80",count=1)



