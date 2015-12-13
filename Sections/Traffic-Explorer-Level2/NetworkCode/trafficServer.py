'''
Simple multithreaded server system used by the NI Raspberry Jam Traffic light activities put together by Andrew Mulholland.
This code runs on the Raspberry Pi inside the traffic light.
A new thread is created for each client connection which simply writes what they send, to a text file which can be read by any system.   

This code can be used for working with any shared resource with a classroom of students, simply has a second Python script which keeps an eye on
the text file.


This file is licenced under the MIT Licence (https://opensource.org/licenses/MIT)


'''
 
import socket
import sys
from thread import *

 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
TEXTFILE = "/home/pi/t.txt"
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#Start listening on socket
s.listen(10)
print 'Socket now listening'
 
#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client
    conn.send('Welcome to the server. Type something and hit enter\n') #send only takes string
     
    #infinite loop so that function do not terminate and thread do not end.
    while True:
         
        #Receiving from client
        data = conn.recv(1024)
        reply = 'OK...' + data
        if not data: 
            break
        print(reply)
	f = open(TEXTFILE, 'w')
	f.write(str(data))
	f.close()
     
    #came out of loop
    conn.close()
 
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
     
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))
 
s.close()
