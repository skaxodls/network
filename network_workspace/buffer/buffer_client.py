import socket
import person2_pb2

def start_client(host, port):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((host, port))

    person=person2_pb2.Person2()
    person.name="Charlie"
    person.age=25

    data=person.SerializeToString()
    client_socket.sendall(data)

if __name__ == "__main__":
  start_client('localhost', 62345)
