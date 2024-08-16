from socket import socket, AF_INET, SOCK_STREAM, SHUT_WR

def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    try:
        serversocket.bind(('localhost', 9000))
        serversocket.listen(5) # queue upto 5
        print('Server started on port 9000')
        while True:
            clientsocket, address = serversocket.accept()
            
            req = clientsocket.recv(5000).decode()
            reqlist = req.split('\n')

            if len(reqlist) > 0:
                print(reqlist[0])
            
            data = 'HTTP/1.1 200 OK\r\n'
            data += 'Content-Type: text/html; charset=utf-8\r\n'
            data += '\r\n'
            data += '''<html><head><title>http.py</title></head>
                        <body>
                            <h1>Hello World</h1>
                        </body>
                       </html>\r\n\r\n'''
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)
    except KeyboardInterrupt:
        print('\nShutting down...\n')
    except Exception as e:
        print('Error:')
        print(e)
    finally:
        serversocket.close()

createServer()


