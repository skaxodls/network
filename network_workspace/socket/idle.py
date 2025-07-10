import socket

def start_TCP_client(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.connect((host, port))
      
      s.sendall(b'Hello, Server!')
      data=s.recv(1024)
      print(f'Recieved : {data.decode()}')

host = 'localhost'
port= 62345
start_TCP_client(host, port)
