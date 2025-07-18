import socket

def handle_request(request):
    headers=request.split('\n')
    filename=headers[0].split()[1]#요청된 파일 이름 추출
    if filename=='/':
        filename='/index.html' #기본 파일 설정

    try:
        with open('.'+filename, 'rb') as file:
            content=file.read()
            response='HTTP/1.0 200 OK\n\n' + content.decode()
    except FileNotFoundError:
        response = 'HTTP/1.0 404 NOT FOUND\n\n FILE NOT FOUND'

    return response

def run_http_server(host='127.0.0.1',port=8000):
    server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    server_socket.bind((host,port))
    server_socket.listen(1)

    print(f"Listening on {host}:{port}...")

    while True:
        client_connection, client_address=server_socket.accept()
        request=client_connection.recv(1024).decode()
        print(f"Received request from {client_address}")

        response=handle_request(request)
        client_connection.sendall(response.encode())
        client_connection.close()

if __name__=="__main__":
    run_http_server()
