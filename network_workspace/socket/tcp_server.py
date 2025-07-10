import socket

def start_TCP_server(host,port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.bind((host, port))
      s.listen()
      print(f"Server listening on {host}:{port}")

      while True:
        conn, addr= s.accept()
        with conn:
          print(f"Connected by {addr}")

          while True:
            data=conn.recv(1024)
            if not data:
              break
            conn.sendall(data.upper())

host='localhost'
port=9999
start_TCP_server(host, port)