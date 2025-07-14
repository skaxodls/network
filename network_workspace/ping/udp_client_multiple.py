import socket
import threading
import time
import random

def udp_client(client_id):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        for i in range(5):
            message=f"message {i+1} from client{client_id}"
            client_socket.sendto(message.encode(),('localhost',12345))
            
            data, _=client_socket.recvfrom(1024)
            print(f"Client {client_id} received: {data.decode()}")
            time.sleep(random.random())


def run_clients(num_clients):
    threads=[]
    for i in range(num_clients):
        thread=threading.Thread(target=udp_client, args=(i+1, ))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__=="__main__":
    run_clients(3)