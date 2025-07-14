import socket

def udp_simple_client():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        message="hello, UDP"
        client_socket.sendto(message.encode(), ('localhost',12345))

        data, _=client_socket.recvfrom(1024)
        print(f"Received from server: {data.decode()}")


if __name__=="__main__":
    udp_simple_client()