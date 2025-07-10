import socket
import threading
import json

def handle_client(conn, addr):
  print(f"New connection from {addr}")
  while True:
    try:
      data=conn.recv(1024)
      
      if not data: 
        break
      
      request=json.loads(data.decode())
      
      if request['action']=='echo':
        response={'status': 'success', 'data': request['data']}
      elif request['action']=='reverse':
        response={'status': 'success', 'data': request['data'][::-1]} 
      else: 
        response={'status': 'error', 'message':'invalid action'}
      
      conn.sendall(json.dumps(response).encode())
    
    except json.JSONDecodeError:
      response={'status': 'error', ' message': 'invalid JSON'}
      conn.sendall(json.dumps(response).encode())
    except Exception as e: 
      print(f"Error handling client {addr}: {e}")
      break

  print(f"Connection from {addr} closed")
  conn.close()

def start_server(host, port):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    s.bind((host, port))
    s.listen()
    print(f"Server listening on {host}:{port}")

    while True:
      conn, addr=s.accept()
      thread=threading.Thread(target=handle_client, args=(conn,addr))
      thread.start()

if __name__=="__main__":
  start_server('localhost', 8888)