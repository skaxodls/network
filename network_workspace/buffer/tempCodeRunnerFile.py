def receive_large_data(sock, buffer_size=1024):
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