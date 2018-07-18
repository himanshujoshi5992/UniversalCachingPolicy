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
contenttypes={}
count = 0
macaddr = "00:00:00:00:00:01"

def GET_print(packet):

    # To extract the url out of the GET request #

    url = "".join(packet.sprintf("{Raw:%Raw.load%}").split(r"\r\n"))
    content_name = url.split()
    
    extract_url(content_name)
    #return "\n".join((
    #    stars(40) + "GET PACKET" + stars(40),
    #    "\n".join(packet.sprintf("{Raw:%Raw.load%}").split(r"\r\n")),
    #    stars(90)))
    return ""
    
def extract_url(data):
    
    if len(data) >= 0:
        #print "Url:" + data[1]
 
        if data[1] not in contenttypes:
            
            contenttypes[data[1]] = {}
            contenttypes[data[1]]["Count"] = 1
            contenttypes[data[1]]["mac"] = macaddr
        else:
            contenttypes[data[1]]["Count"] += 1
            #contenttypes[data[1]]["mac"] = macaddr
        

    #print 'Content types =========================================>'
    #print contenttypes
    send_data(contenttypes)


def send_data(data):
    #print "hello"
    s = socket.socket() 
    
    port = 65531
    s.connect(('10.0.2.15', port)) # Connecting to the controller.
    c = json.dumps(contenttypes) 
    stringdata = str(c)
    #print 'sent ===>'
    #print stringdata
    s.send(stringdata)
    print s.recv(1024)
    #contenttypes={}
    #s.close()


while True:
    #t = Timer(15.0, send_data,[contenttypes])
    #t.start()
    
    sniff(
	    prn=GET_print,
	    lfilter=lambda p: "GET" in str(p),
	    filter="tcp port 80",count=1)



