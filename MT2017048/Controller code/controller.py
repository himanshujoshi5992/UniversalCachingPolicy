
import socket               
from collections import Counter
from threading import Timer
from uuid import getnode as get_mac
import time


s = socket.socket()
print "Socket successfully created"
cont_popularity = 0
port = 65531    
tempdata = {'content0':{'Count':0,'mac':'FF:FF:FF:FF:FF:FF'}}
s.bind(('', port))  
"socket binded to %s" %(port)
s.listen(35)     
print "Controller is listening..."  


def dump_data():
	s2 = socket.socket() 
	port2 = 65534
	s2.connect(('192.168.122.1', port2))
	# Feature preparation step
	for data in tempdata:
		#data = tempdata[0]
		#print '---------------tempdata---------------'
		#print tempdata
		#print '--------------------------------------'
		print '------------------data----------------'
		print data
		print '--------------------------------------'
		content_type = data[7:]
		s1_reqtype = 0
		s1_overall = 0
		s2_reqtype = 0
		s2_overall = 0
		s3_overall = 0
		s3_reqtype = 0
		s4_reqtype = 0
		s4_overall = 0
		s5_reqtype = 0
		s5_overall = 0
		s6_reqtype = 0
		s6_overall = 0
		total_req = 0
		for tempdata[data]["mac"] in tempdata[data]["mac"]:
			s1_reqtype += tempdata[data]["Count"]
			s1_overall += s1_reqtype 
			total_req += s1_overall 

		for tempdata[data]["mac"] in tempdata[data]["mac"]:
			s2_reqtype += tempdata[data]["Count"] 
			s2_overall += s2_reqtype 
			total_req += s2_overall 

		for tempdata[data]["mac"] in tempdata[data]["mac"]:
			s3_reqtype += tempdata[data]["Count"] 
			s3_overall += s3_reqtype 
			total_req += s3_overall 

		for tempdata[data]["mac"] in tempdata[data]["mac"]:
			s4_reqtype += tempdata[data]["Count"] 
			s4_overall += s4_reqtype 
			total_req += s4_overall 

		for tempdata[data]["mac"] in tempdata[data]["mac"]:
			s5_reqtype += tempdata[data]["Count"] 
			s5_overall += s5_reqtype 
			total_req += s5_overall 

		for tempdata[data]["mac"] in tempdata[data]["mac"]:
			s6_reqtype += tempdata[data]["Count"] 
			s6_overall += s6_reqtype 
			total_req += s6_overall 
		# Record is the test vector given to the deep learning algorithm
		record = content_type+','+`s1_reqtype`+','+`s2_reqtype`+','+`s3_reqtype`+','+`s4_reqtype`+','+`s5_reqtype`+','+`s6_reqtype`+','+`s1_overall`+','+`s2_overall`+','+`s3_overall`+','+`s4_overall`+','+`s5_overall`+','+`s6_overall`+','+`total_req`
		#popularity = DLCM.predict(record)
		
		
		print '========Record sent for popularity prediction=======>'
		print (record)
		print '====================================================>'
		s2.send(record)

		#time.sleep(5)	

		print '================Content popularity==================>'
		cont_popularity = s2.recv(1024)
		print cont_popularity
		print '====================================================>'
		break
	return cont_popularity
				 
while True:

	# Establish connection with client.
	c, addr = s.accept() 

	data = c.recv(1024)

	dict2 = eval(data)
	#print '============Received json ===========>'
	#print dict2
	#print '=====================================>'
	#tempdata = dict(Counter(tempdata) + Counter(dict2))
	for key in dict2:
		if key not in tempdata:
			tempdata[key] = dict2[key]
		elif dict2[key]["mac"] not in tempdata[key]["mac"]:
			tempdata[key] = dict2[key]
		else:
			tempdata[key]["Count"] = tempdata[key]["Count"] + dict2[key]["Count"]

	#print 'This is tempdata ===================>'
	#print tempdata
	print 'Got connection from', addr
	#print(addr.getsockname()[0])
	# send a thank you message to the client. 

	popularity = dump_data()
	c.send('Content popularity is '+str(popularity))
	c.close()

	#t = Timer(30.0, dump_data)
	#t.start() 
	# Close the connection with the client
	#time.sleep(30)
	#c.close()



		
