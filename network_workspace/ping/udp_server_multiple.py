import socket
import time
import random

def udp_server_multiple():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind(('localhost',12345))
        print("UDP server is running")

        while True:
            data, addr=server_socket.recvfrom(1024)
            print(f"Received from {addr}: {data.decode()}")

            response=f"Server received: {data.decode()}"

            time.sleep(random.random())

            server_socket.sendto(response.encode(), addr)
if __name__=="__main__":
    udp_server_multiple()