
import socket
from deeplearningcm import DLCM

deep_learning = DLCM()
deep_learning.training()

s = socket.socket()
print "Socket successfully created"

port = 65534

s.bind(('', port))
print "socket binded to %s" %(port)
s.listen(35)
print "socket is listening"
while True:

   # Establish connection with client.
   c, addr = s.accept()
   data = c.recv(1024)
   print data
   header="Content_type,Router1_type_req,Router2_type_req,Router3_type_req,Router4_type_req,Router5_type_req,Router6_type_req,Router1_total_req,Router2_total_req,Router3_total_req,Router4_total_req,Router5_total_req,Router6_total_req,Request_at_allnode"+'\n'
   file = open("predict.csv","w")
   fullstr = header + data
   file.write(fullstr)
   file.close()

   popularity = deep_learning.predict()

   print '===================================='
   print popularity
   print '===================================='

   print 'Got connection from', addr

   
   l = popularity.tolist()
   print l
   for p in l:
      count = p.index(1.0)
   count += 1
      #count = p.index(1)

   # send a thank you message to the client.

   print "Popularity sent ======================================="

   c.send(str(count))
   print count
   # Close the connection with the client
   c.close()
