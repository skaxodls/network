import socket

def send_request(host, port, path):
    client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((host, port))

    request=f'GET {path} HTTP/1.0\nHost: {host}\n\n'
    client_socket.send(request.encode())

    response='' 
    while True:
        data=client_socket.recv(1024)
        if not data:
            break
        response+=data.decode()

        client_socket.close()
        return response
    
def parse_response(response):
    headers, body= response.split('\n\n',1)
    status_line=headers.split('\n')[0]
    status_code=int(status_line.split()[1])
    return status_code, body

def run_http_client():
    response=send_request('127.0.0.1', 8000, '/')
    status_code, body=parse_response(response)
    print(f"Status Code: {status_code}")
    print(f"Body: \n{body[:100]}")

if __name__=="__main__":
    run_http_client()