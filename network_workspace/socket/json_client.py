import socket
import json

def start_client(host, port):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    while True: 
      action =input("Enter actin (echo/reverse) or 'quit' to exit: ")
      if action.lower() =='quit':
        break
      data=input ("Enter data: ")
      request={'action': action, 'data': data}
      s.sendall(json.dumps(request).encode())
      response=s.recv(1024)
      print(f"Received :{json.loads(response.decode())}")

if __name__=="__main__":
  start_client('localhost', 8888)