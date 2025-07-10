import socket

def set_socket_buffer_size(sock, send_size, recv_size):
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF,send_size)
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, recv_size)


def get_socket_buffer_size(sock):
  send_size=sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
  recv_size=sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
  return send_size, recv_size

def receive_large_data(sock, buffer_size=10240):
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

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        set_socket_buffer_size(server_socket,65536,65536)
        send_size, receive_size=get_socket_buffer_size(server_socket)
        print(f"Server buffer sizes - Send: {send_size}, Receive: {receive_size}")

        server_socket.bind(('localhost',62345))
        server_socket.listen()
        print("Server is listen")

        client_socket, addr =server_socket.accept()
        with client_socket:
           print(f"Connected by {addr}")
           data = receive_large_data(client_socket)
           print(f"Received {len(data)} bytes of data")
           send_large_data(client_socket, data.upper())

if __name__ == "__main__":
    start_server()