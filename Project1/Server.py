import sys
from socket import *

# create socket for server to listen - IPv4, TCP
serverSocket = socket(AF_INET, SOCK_STREAM)
# assign a port number
serverPort = 8080
# bind socket w/ IP and port to listen
serverSocket.bind(('', serverPort))
# unique to TCP - makes socket ready for accepting connections
serverSocket.listen(1)

while True:
    # Establish the connection
    print('Ready to serve...')
    # accepts incoming connection request from TCP client
    connectionSocket, addr = serverSocket.accept()
    try:
        # returns received data as bytes object
        message = connectionSocket.recv(1024)
        #  splits string into a list of substrings based on whitespace
        filename = message.split()[1]
        # open file
        f = open(filename[1:])
        # read file content
        outputdata = f.read()
        # server console confirmation
        print("200 OK")
        # send ok status code to client
        connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode())
        # Send the entire HTML content at once
        connectionSocket.sendall(outputdata.encode())

        # ORIGINAL CODE -> Printed HTML code without formatting
        # Send the content of the requested file to the client
        # for i in range(0, len(outputdata)):
        #   connectionSocket.send(outputdata[i].encode()) #send html contents to client
        # connectionSocket.send("\r\n".encode()) #new line at end of content

        # close client connection
        connectionSocket.close()

    # IOError = incorrect file name/location
    except IOError:
        # server console confirmation
        print("404 not found")
        # send error status code to client
        connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n'.encode())
        # close client connection
        connectionSocket.close()

    # close server socket
    serverSocket.close()
    # Terminate the program after sending the corresponding data
    sys.exit()
