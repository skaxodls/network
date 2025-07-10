import socket

def set_socket_buffer_size(sock, send_size, recv_size):
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF,send_size)
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, recv_size)


def get_socket_buffer_size(sock):
  send_size=sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
  recv_size=sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
  return send_size, recv_size


def start_client():
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    # Set the buffer sizes for the client socket
    set_socket_buffer_size(client_socket, 65536, 65536)
    send_size, receive_size = get_socket_buffer_size(client_socket)
    print(f" Client buffer sizes - Send{send_size}, Receive: {receive_size}")

    client_socket.connect(('localhost', 62345))  # Connect to the server
    client_socket.sendall(b"Hello, Size Buffer Client")
    data=client_socket.recv(1024)

    print(f"Received: {data.decode()}")

if __name__ == "__main__":
    start_client()  # Example usage
