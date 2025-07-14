import socket

def udp_simple_server():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind(('localhost',12345))
        print("UDP server is listening")

        while True: 
            data, addr=server_socket.recvfrom(1024)
            print(f"Received message from {addr}: {data.decode()}")
            
            server_socket.sendto(data.upper(),addr)


if __name__=="__main__":
    udp_simple_server()
