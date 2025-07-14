import socket
import select
import struct


def non_blocking_send(sock, data):
  data_length=struct.pack('!I', len(data))
  sock.sendall(data_length)
  data_to_send=data
  while data_to_send:
    try:
      sent=sock.send(data_to_send)
      data_to_send=data_to_send[sent:]
    except BlockingIOError:
      select.select([],[sock],[],5)
    # except socket.error as e:
    #   if e.errno != socket.EAGAIN and e.errno != socket.EWOULDBLOCK:
    #     raise
    #   print("Send buffer is full, waiting")
    #   select.select([],[sock], [])

def non_blocking_receive(sock, length,buffer_size=1024):
  data=b""
  while len(data) < length: 
    try:
      part=sock.recv(min(buffer_size, length-len(data)))
      if not part:
        print("Connection closed by peer")
        break
      data += part
    except BlockingIOError:
      select.select([sock],[],[],5)
  return data

    # try:
    #   part=sock.recv(buffer_size)
    #   if not part:
    #     break
    #   data+=part
    # except socket.error as e:
    #   if e.errno != socket.EAGAIN and e.errno != socket.EWOULDBLOCK:
    #     raise
    #   print("Receive buffer is empty, waiting")
    #   select.select([sock],[] ,[])
  return data

def start_client():
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect(('localhost', 62345))
    client_socket.setblocking(False)

    large_data=b"hello, non-blocking TCP!"*100000 # 약 2.6MB
    non_blocking_send(client_socket, large_data)


    #데이터 길이를 먼저 수신
    while True:
      try:
        data_length_packed=client_socket.recv(4)
        if data_length_packed:
          data_length=struct.unpack('!I',data_length_packed)[0]
          received_data=non_blocking_receive(client_socket,data_length)
          if received_data:
            print(f"Received {len(received_data)} bytes")
          else:
            print("No data received or connection closed")
      except BlockingIOError:
        select.select([client_socket],[],[],5)
      client_socket.close()
      print("Conntion closed gracefully")

    # received_data=non_blocking_receive(client_socket)
    # print(f"Received {len(large_data)} bytes")

if __name__=="__main__":
    start_client()  # Example usage