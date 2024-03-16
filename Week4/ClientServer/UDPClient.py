from socket import *

def cust_port_num():
    portNum = input('Input port number: ')
    if int(portNum) < 1024:
        print("Port number too small. Try again.")
        cust_port_num()
    return int(portNum)


serverName = '0.0.0.0' #switch to own IP
serverPort = cust_port_num()
clientSocket = socket(AF_INET, SOCK_DGRAM)
#clientSocket.bind(('', 5432))
message = input('Input lowercase sentence:')
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()

