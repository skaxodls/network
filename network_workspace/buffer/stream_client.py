import socket
import struct

def start_client():
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect(('localhost', 62345))  # Connect to the server
    send_message(client_socket, "Hello, Stream Socket")
    response =receive_message(client_socket)
    print(f"Received : {response}")

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
  
if __name__ == "__main__":
    start_client()  # Example usage