import socket
import select

def improved_client(host,port,message,timeout=5):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            s.connect((host, port))

            total_sent=0
            #message=message.encode()
            while total_sent<len(message):
                sent=s.send(message[total_sent:])
                if sent ==0:
                    raise RuntimeError("Socket connection broken")
                total_sent+=sent

            chunks = []
            while True:
              readable,_,_=select.select([s],[],[],timeout)
              if readable:
                  chunk=s.recv(1024)
                  if not chunk:
                      break
                  chunks.append(chunk)
              else: 
                if chunks:
                  break
                else: 
                  raise socket.timeout("Recieve operation timed out")
    except socket.timeout:
      print("Connection timed out")
    except ConnectionRefusedError:
        print("Contection refused. Is the server running?")
    except Exception as e:
        print(f"An error occurred: {e}")

improved_client('localhost', 9999, b'Hello, Server!') 

