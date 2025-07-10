import socket
import threading

def handle_client(conn, addr):
    print(f"New connection from {addr}")

    try:
        while True:
            data=conn.recv(1024)
            if not data:
                break
            response=data.decode()[::-1].encode()
            conn.sendall(response)
            
    except Exception as e:
        print(f"Error handling client {addr}: {e}")
    finally: 
        print(f"Connection from {addr} closed")
        conn.close()
    
def start_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")

        while True: 
            conn, addr=s.accept()
            thread=threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()

if __name__=="__main__":
    start_server('localhost', 8888)
