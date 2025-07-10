import socket

def set_socket_buffer_size(sock, send_size, recv_size):
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF,send_size)
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, recv_size)


def get_socket_buffer_size(sock):
  send_size=sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
  recv_size=sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
  return send_size, recv_size

def start_server():
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    set_socket_buffer_size(server_socket, 65536, 65536)
    send_size, recv_size = get_socket_buffer_size(server_socket)
    print(f"Server buffer sizes - Send: {send_size}, Receive: {recv_size}")

    server_socket.bind(('localhost', 62345 ))
    server_socket.listen()
    print("Server is listening")

    client_socket, addr = server_socket.accept()
    with client_socket:
      print(f"Connected by {addr}")
      while True:
        data = client_socket.recv(1024)
        if not data:
          break
        client_socket.sendall(data.upper())

if __name__ == "__main__":
    start_server()  # Example usage