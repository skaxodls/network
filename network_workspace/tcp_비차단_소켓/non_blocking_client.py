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

def start_client():
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect(('localhost', 62345))
    client_socket.setblocking(False)

    large_data=b"hello, non-blocking TCP!"*100000 # 약 2.6MB
    non_blocking_send(client_socket, large_data)
    print(f"Received {len(large_data)} bytes")

if __name__=="__main__":
    start_client()  # Example usage