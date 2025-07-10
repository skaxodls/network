import socket

def start_client(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.connect((host,port))
      while True:
          message=input("Enter message(or 'quit' to exit):")
          if message.lower()=='quit':
            break
          
          s.sendall(message.encode())
          data=s.recv(1024)
          print(f"Received response: {data.decode()}")


if __name__=="__main__":
    start_client('localhost', 8888)