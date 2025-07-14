import socket
import struct

def udp_multicast_sender():
    multicast_group=('224.3.29.71',10000)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sender_socket:
        ttl=struct.pack('b',1)
        sender_socket.setsockopt(socket.IPPROTO_IP,socket.IP_MULTICAST_TTL,ttl)

        message="hello multicast group"
        sender_socket.sendto(message.encode(),multicast_group)
        print(f"Multicast message sent: {message}")


if __name__=="__main__":
    udp_multicast_sender()