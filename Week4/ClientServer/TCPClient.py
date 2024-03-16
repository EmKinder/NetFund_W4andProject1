from socket import *
def cust_port_num():
    portNum = input('Input port number: ')
    if int(portNum) < 1024:
        print("Port number too small. Try again.")
        cust_port_num()
    return int(portNum)

serverName = '0.0.0.0' #switch to own IP
serverPort = cust_port_num()
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input('Input a lowercase sentence: ')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From Server: ' + modifiedSentence.decode())
clientSocket.close()
print('complete')
