#server
import socket

def main():
    host = '127.0.0.1'
    port = 50001
    bufsize = 1024

    server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, \
            proto=0, fileno=None)
    serveraddr = (host, port)
    server.bind(serveraddr)
    server.listen()
    (connection, clientaddr) = server.accept()

    msg = 'Hey, I am the server. What\'s up, client?'
    buf = msg.encode()
    connection.send(buf)



    buf = connection.recv(bufsize)
    msg = buf.decode()
    print('Client says: \'' + msg + '\'')

    connection.close()
    server.close()

if __name__ == '__main__':
    main()