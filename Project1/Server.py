import sys
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM) #create socket for server to listen - IPv4, TCP
serverPort = 8080 #assign a port number
serverSocket.bind(('', serverPort)) #bind socket w/ IP and port to listen
serverSocket.listen(1) #unique to TCP - makes socket ready for accepting connections

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() #accepts incoming connection request from TCP client
    try:
        message = connectionSocket.recv(1024) #returns recieved data as bytes object
        filename = message.split()[ 1] #...
        f = open(filename[1:]) #open file
        outputdata = f.read() #read file content
        print("200 OK") #server console confirmation
        connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode()) #send ok status code to client
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode()) #send html contents to client
        connectionSocket.send("\r\n".encode()) #new line at end of content
        connectionSocket.close() #close client connection
    except IOError: #IOError = incorrect file name/location
        print("404 not found") #server console confirmation
        connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n'.encode()) #send error status code to client
        connectionSocket.close() #close client connection
    serverSocket.close() #close server socket
    sys.exit() #Terminate the program after sending the corresponding data
