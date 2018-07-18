#!/usr/bin/env python

import httplib
import sys
import time
from random import *

#get http server ip
http_server = sys.argv[1]
#create a connection
conn = httplib.HTTPConnection(http_server)

while 1:
    #cmd = raw_input('input command (ex. GET index.html): ')
    #cmd = cmd.split()
    number = randint(1,5)
    #number = 1
    print('Requesting content '+`number`)
    cmd = 'content'+`number`
    if cmd == 'exit': #tipe exit to end it
        break
    
    #request command to server
    conn.request('GET', cmd)

    #get response from server
    rsp = conn.getresponse()
    
    #print server response and data
    print(rsp.status, rsp.reason)
    data_received = rsp.read()
    print(data_received)
    x = randint(1, 10)
    print(x)
    time.sleep(x)
conn.close()
