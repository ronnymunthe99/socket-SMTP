from socket import *
import ssl
import base64
import time

msg = "\r\n Ronny Jelek!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ("smtp.gmail.com",465)

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket = ssl.wrap_socket(clientSocket,ssl_version=ssl.PROTOCOL_SSLv23)
clientSocket.connect(mailserver)
recv = clientSocket.recv(1024)
recv = recv.decode()
print (recv)
if recv[:3] != '220':
	print ('220 reply not received from server.')
	
# Send HELO command and print server response.
heloCommand = "HELO Alice\r\n"
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024)
recv1 = recv1.decode()
print (recv1)
if recv1[:3] != '250':
     print ('250 reply not received from server.')
	 
#Info for username and password
username="ronnymunthe99@@gmail.com"
password="ronidomi20"
base64_str = ("\x00"+username+"\x00"+password).encode()
base64_str =base64.b64encode(base64_str)
authMsg = "AUTH PLAIN".encode()+base64_str+"\r\n".encode()
clientSocket.send(authMsg)
recv_auth = clientSocket.recv(1024)
print(recv_auth.decode())

# Send MAIL FROM command and print server response.
mailFromCommand = "MAIL FROM :<ronnymunthe99@@gmail.com>\r\n"
clientSocket.send(mailFromCommand.encode())
recv2 = clientSocket.recv(1024)
recv2 = recv2.decode()
print("After MAIL FROM command: "+recv2)

# Send RCPT TO command and print server response. 
rcptToCommand = "RCTP To:<jonathan.nicholas.14052001@gmail.com>\r\n"
clientSocket.send(rcptToCommand.encode())
recv3 = clientSocket.recv(1024)
recv3 = recv3.decode()
print("After RCTP TO command: "+recv3)

# Send DATA command and print server response. 
dataCommand = "DATA\r\n"
clientSocket.send(dataCommand.encode())
recv4 = clientSocket.recv(1024)
recv4 = recv4.decode()
print("After DATA command: "+recv4)

# Send message data.
clientSocket.send(msg.encode())

# Message ends with a single period.
clientSocket.send(endmsg.encode())
recv_msg = clientSocket.recv(1024)
print("Response after sending message body:"+recv_msg.decode())

# Send QUIT command and get server response.
quit = "QUIT\r\n"
clientSocket.send(quit.encode())
recv5 = clientSocket.recv(1024)
print(recv5.decode())
clientSocket.close()
