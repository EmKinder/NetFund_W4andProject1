from socket import *

def cust_port_num():
    portNum = input('Input port number: ')
    if int(portNum) < 1024:
        print("Port number too small. Try again.")
        cust_port_num()
    return int(portNum)

serverPort = cust_port_num()
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    print(clientAddress)
