import socket
import struct

def udp_multicast_receiver():
    multicast_group='224.3.29.71'
    server_address=('',10000)

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as receiver_socket:
        #소켓을 주소와 포트에 바인딩
        receiver_socket.bind(server_address)
        
        #멀티캐스트 그룹 가입
        group=socket.inet_aton(multicast_group)
        mreq=struct.pack('4sL', group, socket.INADDR_ANY)
        receiver_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

        print("Waiting for multicast messages")
        while True: 
            data,address=receiver_socket.recvfrom(1024)
            print(f" Received multicast from {address} : {data.decode()}")


if __name__=="__main__":
    udp_multicast_receiver()