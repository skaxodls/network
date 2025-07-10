import socket
import person2_pb2

def start_server(host,port):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Server listening on {host}:{port}")

    while True:
      client_socket, addr =server_socket.accept()
      with client_socket:
        print(f"Connection from {addr}")
        data= client_socket.recv(1024)
        person=person2_pb2.Person2()
        person.ParseFromString(data)

        print(f"Received : Name={person.name}, Age={person.age}")

if __name__ == "__main__":
    start_server('localhost', 62345)  # Example usage