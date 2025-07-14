import socket
import struct
import random
import time

def stock_price_server():
    multicast_group=('224.3.29.71',10000)

    with socket.socket(socket.AF_INET,socket.SOCK_DGRAM, socket.IPPROTO_UDP) as sock:
        ttl=struct.pack('b',1)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

        while True:
            stock_price=random.uniform(100,200)
            message=f"AAPL: ${stock_price:.2f}"

            sock.sendto(message.encode(), multicast_group)
            print(f"Sent: {message}")

            time.sleep(5)
if __name__=="__main__":
    stock_price_server()
