import socket
import ssl

def secure_ssl_client():
    context=ssl.create_default_context()
    context.set_ciphers('ECDHE+AESGCM')
    context.minimum_version=ssl.TLSVersion.TLSv1_2
    context.check_hostname=True
    context.verify_mode=ssl.CERT_REQUIRED

    try:
        
        with socket.create_connection(('www.python.org',443)) as sock:
            with context.wrap_socket(sock, server_hostname='www.python.org') as secure_sock:
                print(f"연결된 서버: {secure_sock.getpeername()}")
                print(f"사용된 TLS 버전: {secure_sock.version()}")
                print(f"사용된 암호 스위트: {secure_sock.cipher()}")

                print("서버 인증서 검증 완료")

                secure_sock.sendall(b"GET / HTTP/1.1\r\nHost: www.python.org\r\n\r\n")
                data=secure_sock.recv(1024)
                print(f" 서버 응답 {data[:100]}...")
    except ssl.SSLError as e:
        print(f"SSL 오류 발생: {e}")
    except ssl.CertificateError as e:
        print(f"인증서 오류 발생: {e}")

if __name__=="__main__":
    secure_ssl_client()