import socket
import select

def non_blocking_send(sock, data):
  data_to_send=data
  while data_to_send:
    try:
      sent=sock.send(data_to_send)
      data_to_send=data_to_send[sent:]
    except socket.error as e:
      if e.errno != socket.EAGAIN and e.errno != socket.EWOULDBLOCK:
        raise
      print("Send buffer is full, waiting")
      select.select([],[sock], [])

def non_blocking_receive(sock, buffer_size=4096):
  data=b""
  while True :
    try:
      part=sock.recv(buffer_size)
      if not part:
        break
      data+=part
    except socket.error as e:
      if e.errno != socket.EAGAIN and e.errno != socket.EWOULDBLOCK:
        raise
      print("Receive buffer is empty, waiting")
      select.select([sock],[] ,[])
  return data

def start_server(host, port):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((host, port))
    server_socket.listen()
    server_socket.setblocking(False)
    print("Non-blocking server is listening")

    while True:
      try: 
        client_socket, addr = server_socket.accept()
        client_socket.setblocking(False)
        print(f"Connected by {addr}")

        received_data=non_blocking_receive(client_socket)
        print(f"Received {len(received_data)} bytes")
        non_blocking_send(client_socket, received_data.upper())
      except socket.error as e:
        if e.errno != socket.EAGAIN and e.errno != socket.EWOULDBLOCK:
          raise
        
if __name__=="__main__":
    start_server('localhost', 62345)  # Example usage