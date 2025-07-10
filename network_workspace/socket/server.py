import socket

def start_UDP_server(host, port):
  with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
    s.bind((host, port))
    print(f"UDP server listening on {host}:{port}")

    while True:
      data, addr=s.recvfrom(1024)
      print(f"received message from {addr}: {data.decode()}")
      s.sendto(data.upper(),addr)
      
start_UDP_server('localhost', 9999)

