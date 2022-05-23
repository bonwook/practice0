import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP

google_ip = socket.gethostbyname("google.com") #dns서버를 통해 ip를 알아냄
sock.connect((google_ip,80))

sock.send("GET / HTTP/1.1\n".encode()) #binary 값으로
sock.send("\n".encode()) #약속에 의해 정의된것.
buffer = sock.recv(4096)
buffer = buffer.decode().replace("\r\n", "\n")
sock.close()
print(buffer)
