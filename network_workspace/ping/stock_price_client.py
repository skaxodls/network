import socket
import struct

def stock_price_client():
    multicast_group='224.3.29.71'
    server_address=('',10000)

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(server_address)

        group =socket.inet_aton(multicast_group)
        mreq=struct.pack('4sL',group,socket.INADDR_ANY)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

        print("Waiting for stock price updates")
        while True: 
            data,address=sock.recvfrom(1024)
            print(f"Recevied : {data.decode()} from {address}")

if __name__=="__main__":
    stock_price_client()