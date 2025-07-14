# import socket
# import time
# import struct

# def udp_ping_client(count=4):
#     with socket.socket(socket.AF_INET,socket.SCOK_DGRAM) as client_socket:
#     client_socket.settimeout(1.0)

#     for i in range(count):
#         start_time=time.time()
#         message=struct.pack('!d',start_time)

#         try: 
#             client_socket.sendto(message,('localhost',12345))
#             data,_=client_socket.recvfrom(1024)
#             end_time=time.time()

#             send_time=struct.unpack('!d',data)[0]
#             rtt=(end_time-send_time)*1000
#             print(f"Ping {i+1}: RTT={rtt:3f}ms")
#         except:
