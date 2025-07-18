import socket
import threading

class HTTPServer:
    def __init__(self, host='127.0.0.1',port=8000):
        self.host=host
        self.port=port
        self.routes={}

    def route(self, path, method='GET'):#get은 default값
        def decorator(f):
            self.routes[(path,method)]=f
            return f
        return decorator
    
    def handle_request(self, request):
        headers=request.split('\r\n')
        method, path, _=headers[0].split()

        if(path,method) in self.routes:
            handler=self.routes[(path, method)]
            response=handler(headers)
        else:
            response=('HTTP/1.0 404 NOT FOUND\r\n\r\n'
                    'NOT FOUND')
        return response

    def run(self):
        server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        server_socket.bind((self.host, self.port))
        server_socket.listen(1)
        print(f"Listening on {self.host}:{self.port}...")

        while True:
            client_conn, client_addr=server_socket.accept()
            client_thread=threading.Thread(target=self.handle_client, args=(client_conn, client_addr))
            client_thread.start()
    
    def handle_client(self, client_conn, client_addr):
        request=client_conn.recv(1024).decode()
        print(f'Received request from {client_addr}')

        response=self.handle_request(request)
        client_conn.sendall(response.encode())
        client_conn.close()

app = HTTPServer()

@app.route('/')
def index(headers):
    return('HTTP/1.0 200 OK\r\n\r\n'
           '<h1>Welcom to the Home Page</h1>')

@app.route('/about')
def about(headers):
    return ('HTTP/1.0 200 OK\r\n\r\n'
            '<h1>About_US</h1>')

@app.route('/api/data', method='POST')
def api_data(headers):
    return('HTTP/1.0 201 CREATED\r\n\r\n'
           '{"status" : "success"} ')

if __name__=="__main__":
    app.run()