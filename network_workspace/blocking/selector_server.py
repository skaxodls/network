import socket
import selectors

sel=selectors.DefaultSelector()

def accept(sock, mask):
    conn, addr=sock.accept()
    print(f"Accepted connection from {addr}")
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ,read)

def read(conn, mask):
    data=conn.recv(1024)
    if data:
        print(f"Received data: {data.decode()}")
        conn.send(data)
    else:
        print("Closing connection")
        sel.unregister(conn)
        conn.close()

def start_server_with_selectors():
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost',12345))
    sock.listen(100)
    sock.setblocking(False)
    sel.register(sock, selectors.EVENT_READ, accept)

    while True:
        events=sel.select()
        for key, mask in events:
            callback=key.data
            callback(key.fileobj,mask)
        
start_server_with_selectors()