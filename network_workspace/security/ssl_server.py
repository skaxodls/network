import socket
import ssl

def ssl_server():
    context=ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="server.crt",keyfile="server.key")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(('localhost',8443))
        sock.listen(5)

        with context.wrap_socket(sock, server_side=True) as secure_sock:
            while True: 
                conn, addr =secure_sock.accept()
                with conn:
                    print(f"Connected by {addr}")
                    while True: 
                        #데이터수신
                        data = conn.recv(1024)
                        if not data:
                            break
                        conn.sendall(data.upper())

if __name__=="__main__":
    ssl_server()