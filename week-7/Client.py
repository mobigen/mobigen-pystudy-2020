import socket
import threading
 


def send(client_socket):
    while True :
        message = input()
        if message == 'quit' :
            client_socket.close()
            break
        client_socket.send(message.encode())

def main() :
    host = '127.0.0.1'
    port = 4400
    
    #IPv4 체계, TCP 타입 소켓 객체를 생성
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    th = threading.Thread(target=send, args=(client_socket,))
    th.start()

    while True :

        data = client_socket.recv(1024)
        print(repr(data.decode()))
        
    th.join()
    client_socket.close()
 
if __name__ == '__main__' :
    main()
