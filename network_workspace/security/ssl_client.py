import socket
import ssl

def ssl_client():
    context=ssl.create_default_context()
    context.check_hostname=False#호스트 이름 확인 비활성화
    context.verify_mode=ssl.CERT_NONE#서버 인증서 검증 비활성화

    with socket.create_connection(('localhost',8443)) as sock:#서베에 연결할 기본 소켓을 생성하고 연결으 설정. 이때 CONNECT가 암묵적으로 실행됨
        with context.wrap_socket(sock, server_hostname='localhost') as secure_sock:
            print(f"Connected to {secure_sock.getpeername()}")

            secure_sock.sendall(b"Hello, secure world!")
            data=secure_sock.recv(1024)
            print(f"Received : {data.decode()}")

if __name__=="__main__":
    ssl_client()