import socket
import threading
import time

def blocking_client(num_requests):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.connect(('localhost',12345))
        start_time=time.time()
    
        for i in range(num_requests):
            s.sendall(b'Hello Server!')
            print(f"{i} sent : Hello, server!")
            data=s.recv(1024)
            print(f"{i} received: {data.decode()}")

        end_time=time.time()
        return end_time-start_time
    
def non_blocking_client(num_requests):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.connect(('localhost',12345))
        s.setblocking(False)

        start_time=time.time()
        requests_sent=0
        requests_received=0

        while requests_received<num_requests:
            try:
                if requests_sent <num_requests:
                    s.sendall(b'Hello Server!!')
                    requests_sent+=1
                    print(f"requests_sent: {requests_sent}")
                
                data=s.recv(1024)
                requests_received+=1
                print(f"requests_received: {requests_received}")
            except BlockingIOError:
                print("blockingIOError")
                pass
        
        end_time=time.time()
    return end_time-start_time

def run_benchmark(client_func, num_clients, num_requests):
    threads=[]
    start_time=time.time()
    
    for _ in range(num_clients):
        t=threading.Thread(target=client_func, args=(num_requests,))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
    
    end_time=time.time()
    total_time=end_time-start_time
    
    requests_per_second=(num_clients*num_requests)/total_time
    print(f"{client_func.__name__} : {requests_per_second:.2f} requests/second")

run_benchmark(blocking_client,3, 10)
run_benchmark(non_blocking_client, 3, 10)
    
