import socket
import threading
import time
import random


def tcp_client(client_id):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(('localhost',12345))

        for i in range(5):
            message=f"message {i+1} from client {client_id}"
            client_socket.send(message.encode())
            data=client_socket.recv(1024)
            print(f"Client {client_id} received: {data.decode()}")
            time.sleep(random.random())

def run_clients(num_clients):
    threads=[]

    for i in range(num_clients):
        thread=threading.Thread(target=tcp_client, args=(i+1,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
if __name__=="__main__":
    run_clients(3)