import socket
def udp_file_client():
    CHUNK_SIZE=65507

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        client_socket.sendto(b"request",('localhost',12345))

        file_size_data,_ =client_socket.recvfrom(1024)
        file_size=int(file_size_data.decode())

        received_data=b""
        print(file_size)
        while len(received_data)<file_size:
            chunk, _=client_socket.recvfrom(CHUNK_SIZE)
            received_data+=chunk
            print(len)
        
        with open("received_file.bin",'wb') as file:
            file.write(received_data)
            print(f"File received.Size: {len(received_data)} bytes")

if __name__=="__main__":
    udp_file_client()
