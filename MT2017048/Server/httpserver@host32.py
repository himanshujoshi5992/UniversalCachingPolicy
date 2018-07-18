#!/usr/bin/env python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os

#Create custom HTTPRequestHandler class
class KodeFunHTTPRequestHandler(BaseHTTPRequestHandler):
    
    #handle GET command
    def do_GET(self):
        rootdir = '/home/mininet/acn_project/contents/' #file location
        try:
            
            if self.path.endswith('1'):
                
                f = open(rootdir +self.path) #open requested file

                #send code 200 response
                self.send_response(200)

                #send header first
                self.send_header('Content-type','text-html')
                self.end_headers()

                #send file content to client
                self.wfile.write(f.read())
                f.close()
                return
            elif self.path.endswith('2'):
        		f = open(rootdir + self.path)
        		#self.send_response(200)
        		#self.send_header('Content-type','text-html')
        		#self.end_headers()
        		self.wfile.write(f.read())
        		f.close()
        		return
            elif self.path.endswith('3'):
        		f = open(rootdir + self.path)
        		#self.send_response(200)
        		#self.send_header('Content-type','text-html')
        		#self.end_headers()
        		self.wfile.write(f.read())
        		f.close()
        		return
            elif self.path.endswith('4'):
        		f = open(rootdir + self.path)
        		#self.send_response(200)
        		#self.send_header('Content-type','text-html')
        		#self.end_headers()
        		self.wfile.write(f.read())
        		f.close()
        		return
            elif self.path.endswith('5'):
        		f = open(rootdir + self.path)
        		#self.send_response(200)
        		#self.send_header('Content-type','text-html')
        		#self.end_headers()
        		self.wfile.write(f.read())
        		f.close()
        		return
        except IOError:
            self.send_error(404, 'file not found')
    
def run():
    print('http server is starting...')

    #ip and port of servr
    #by default http server port is 80
    server_address = ('10.0.0.32', 80)
    httpd = HTTPServer(server_address, KodeFunHTTPRequestHandler)
    print('http server is running...')
    httpd.serve_forever()
    
if __name__ == '__main__':
    run()
