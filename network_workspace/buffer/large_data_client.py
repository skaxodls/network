import socket

def receive_large_data(sock, buffer_size=1024):
    data=b""
    while True:
        part=sock.recv(buffer_size)
        if not part:
            break
        data+=part
        if len(part)<buffer_size:
            break
    return data

def send_large_data(sock, data):
    total_sent=0
    while total_sent<len(data):
        sent =sock.send(data[total_sent:])
        if sent==0:
            raise RuntimeError("socket connetion broken")
        total_sent+=sent
        print(f"Sent {total_sent} bytes")

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(('localhost', 62345))  # Connect to the server
        large_data = b"A" * (10**6)  # Example of large data (1 MB)
        print(f"Sending {len(large_data)} bytes of data")
        send_large_data(client_socket, large_data)
        data = receive_large_data(client_socket)
        print(f"Received {len(data)} bytes of data")


if __name__ == "__main__":
    start_client()  # Example usage