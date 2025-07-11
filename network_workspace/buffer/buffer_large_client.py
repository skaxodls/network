import socket
import time

def set_socket_buffer_size(sock, send_size, recv_size):
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF,send_size)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, recv_size)


def get_socket_buffer_size(sock):
    send_size=sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    recv_size=sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
    return send_size, recv_size

def receive_large_data(sock, buffer_size=10240):
    data=b""
    while True:
        part=sock.recv(buffer_size)
        if not part:
            break
        data+=part
        if len(part)<buffer_size:
            break
    return data

def send_large_data(sock, data):
    total_sent=0
    while total_sent<len(data):
        sent =sock.send(data[total_sent:])
        if sent==0:
            raise RuntimeError("socket connetion broken")
        total_sent+=sent
        print(f"Sent {total_sent} bytes")

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        set_socket_buffer_size(client_socket,65536,65536)
        send_size, receive_size=get_socket_buffer_size(client_socket)
        print(f"Client buffer sizes - Send: {send_size}, Receive: {receive_size}")

        client_socket.connect(('localhost',62345))

        large_data=b"A"*(10**6)
        print(f"Sending {len(large_data)} bytes of data")
        start=time.time()
        send_large_data(client_socket, large_data)
        data = receive_large_data(client_socket)
        print(f"Received {len(data)} bytes of data")
        end=time.time()
        print(f"Running time is {end-start}s")

if __name__=="__main__":
    start_client()

#test1 receive large data 함수의 버퍼 크기를 조절해 본다 
#   -> 거의 차이 없음 왜냐? 이 버퍼는 전송받은 데이터를 쌓아두는 역할이라 리소스 할당 많이하면 손실이 줄어듦
#test2 set 할 때 소캣 버퍼의 크기를 조절해 본다
#   -> 차이 약 200배 차이 !이건 소캣에서 데이터를 전송하는 크기여서?