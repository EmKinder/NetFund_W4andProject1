from socket import *
def cust_port_num():
    portNum = input('Input port number: ')
    if int(portNum) < 1024:
        print("Port number too small. sTry again.")
        cust_port_num()
    return int(portNum)

serverPort = cust_port_num()
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    print(addr)
    connectionSocket.close()