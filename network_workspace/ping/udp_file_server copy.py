import socket
import os

def udp_file_server():
    CHUNK_SIZE=65507

    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server_socket:
        server_socket.bind(('localhost',12345))
        server_socket.listen()
        print("UDP file server is running")




        while True:
            conn, addr=server_socket.accept()
            with conn:

                filename = os.path.join(os.path.dirname(__file__), "large_file.bin")
                if not os.path.exists(filename):
                    print(f"File {filename} not found")
                    continue

                file_size=os.path.getsize(filename)
                conn.send(str(file_size).encode())

                with open(filename, 'rb') as file:
                    while True:
                        chunk=file.read(CHUNK_SIZE)
                        if not chunk:
                            break
                        conn.sendto(chunk, addr)
                        print(f"File chunk sent to {addr}")
                    print("파일 전송 완료")

if __name__=="__main__":
    udp_file_server()