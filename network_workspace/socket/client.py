import socket

def start_UDP_client(host, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(message.encode(), (host,port))
        data,_= s.recvfrom(1024)
        print(f"received : {data.decode()}")

start_UDP_client('localhost', 9999, 'hello, UDP server')