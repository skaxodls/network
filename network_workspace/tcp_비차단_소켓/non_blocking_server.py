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

def start_server(host, port):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((host, port))
    server_socket.listen()
    server_socket.setblocking(False)
    print("Non-blocking server is listening")

    while True:
      try: 
        ready_to_read,_,_=select.select([server_socket],[],[],5)
        if server_socket in ready_to_read:
          client_socket, addr = server_socket.accept()
          client_socket.setblocking(False)
          print(f"Connected by {addr}")

        while True:
          try: 
            data_length_packed=client_socket.recv(4)
            if data_length_packed:
              data_length=struct.unpack('!I',data_length_packed)[0]
              received_data=non_blocking_receive(client_socket, data_length)
              if received_data:
                print(f"Received {len(received_data)} bytes")
                non_blocking_send(client_socket, received_data.upper())
              break
          except BlockingIOError:
            select.select([client_socket],[],[],5)
        client_socket.close()

        # received_data=non_blocking_receive(client_socket)
        # print(f"Received {len(received_data)} bytes")
        # non_blocking_send(client_socket, received_data.upper())
      except socket.error as e:
        if e.errno != socket.EAGAIN and e.errno != socket.EWOULDBLOCK:
          raise
        
if __name__=="__main__":
    start_server('localhost', 62345)  # Example usage