import socket
import time

def non_blocking_client_with_timeout(timeout=5):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM)as s:
        s.connect(('localhost',12345))
        s.setblocking(False)

        request=b'Hello, server!'
        response=b''
        start_time=time.time()

        while True:
            if time.time()-start_time>timeout:
                print("Operation timed out")
                break
            try:
                if request:
                    sent=s.send(request)
                    request=request[sent:]
                if not request:
                    data=s.recv(1024)
                    if data:
                        response+=data
                    else:
                        break
            except BlockingIOError:
                pass
        print(f"Request: {response.decode()}")

non_blocking_client_with_timeout()