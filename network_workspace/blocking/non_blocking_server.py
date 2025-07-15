import socket
import select


def non_blocking_server():
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.setblocking(False)
    server.bind(('localhost',12345))
    server.listen()


    #소켓 리스트 및 메시지 큐 초기화 
    inputs=[server]
    outputs=[]
    message_queues={}

    while inputs:
        readable, writable, exceptional=select.select(inputs, outputs, inputs)


        for s in readable:
            if s is server:
                connection, client_address=s.accept()
                connection.setblocking(False)
                inputs.append(connection)
                message_queues[connection]=[]

            else:
                #데이터 수신
                data=s.recv(1024)
                if data:
                    message_queues[s].append(data)
                    if s not in outputs:
                        outputs.append(s)

                else:
                    #연결 종료
                    if s in outputs:
                        outputs.remove(s)
                        inputs.remove(s)
                        s.close()
                        print('close client')
                        del message_queues[s]
        
        for s in writable:
            if message_queues[s]:
                next_msg=message_queues[s].pop(0)
                s.send(next_msg)
            else:
                outputs.remove(s)
        
        #예외 발생 소켓 처리
        for s in exceptional:
            inputs.remove(s)
            if s in outputs:
                outputs.remove(s)
            s.close()
            print("client close")
            del message_queues[s]

non_blocking_server()