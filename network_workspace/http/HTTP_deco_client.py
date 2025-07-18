import socket
import json

class HTTPClient:
    def __init__(self, host, port):
        self.host=host
        self.port=port

    def request(self, method, path, headers=None, body=None):
        if headers is None:
            headers={}

        request=f'{method} {path} HTTP/1.1\r\n'
        request+=f'Host: {self.host}\r\n'

        if body: 
            body_bytes=body.encode() if isinstance(body, str) else json.dumps(body).encode()
            headers['Content-Length']=len(body_bytes)
        
        for key, value in headers.items():
            request +=f'{key}: {value}\r\n'

        request+='\r\n'

        if body:
            request+=body if isinstance(body, str) else json.dumps(body)

        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.host, self.port))
        s.sendall(request.encode())

        response=b''
        while True:
            chunk=s.recv(4096)
            if not chunk:
                break
            response+=chunk
        s.close()
        return self.parse_response(response)
    
    def parse_response(self, response):
        headers, body=response.split(b'\r\n\r\n',1)
        headers=headers.decode()
        status_line=headers.split('\r\n')[0]
        version, status, reason=status_line.split(' ',2)

        return {
            'status': int(status),
            'reason': reason,
            'headers': headers,
            'body': body
        }
    
    def get(self, path, headers=None):
        return self.request('GET',path, headers)
    
    def post(self, path, body, headers=None):
        return self.request('POST', path, headers, body)
    
#사용예
client=HTTPClient('127.0.0.1',8000)

response=client.get('/about')
print(f"Status: {response['status']}")
print(f"Body: {response['body'].decode()} ")

response= client.post('/api/data', {'key':'value'}, {'Content-Type': 'application/json'})
print(f"Status: {response['status']}")
print(f"Body: {response['body'].decode()}")