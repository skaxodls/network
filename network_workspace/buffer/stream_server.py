import socket
import struct

def send_message(sock, message):
  message_len=len(message)
  sock.sendall(struct.pack('!I', message_len))
  sock.sendall(message.encode())

def receive_message(sock):
    raw_msglen=recvall(sock,4)
    if not raw_msglen:
      return None
    msglen=struct.unpack('!I', raw_msglen)[0]
    return recvall(sock, msglen).decode()

def recvall(sock, n):
  data=bytearray()
  while len(data)<n:
      packet=sock.recv(n-len(data))
      if not packet:
        return None
      data.extend(packet)
  return data

def start_server(host, port):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
      server_socket.bind((host, port))
      server_socket.listen()

      print("Server is listening")

      client_socket, addr = server_socket.accept()
      with client_socket:
        print(f"Connected by {addr}")
        
        while True:
          message=receive_message(client_socket)
          if message is None:
            break
          print(f"Received: {message}")
          send_message(client_socket, message.upper())

if __name__ == "__main__":
    start_server('localhost', 62345)  # Example usage