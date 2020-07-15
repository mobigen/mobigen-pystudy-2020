import socket
import threading
import time
from collections import deque
 
conns = []

def sendMessage():
    print('\n')
    while True:
        sendData = input('>>>')
        sendData = '운영자 메세지 : ' + sendData
        for conn in conns :
            try :
                conn.send(sendData.encode('utf-8'))
                #print(conn)
            except :
                #print('연결해제 : %s' % conn)
                conns.remove(conn)


def to_client(client_socket, addr):
    print ('%s에서 접속하였습니다.' % addr[1])
    while True:
        try:
            # 클라이언트로부터 메세지를 가져옴
            data = client_socket.recv(1024)
            if not data :
                print('Disconnected' + addr[0],':',addr[1])
                break
            
            if data == 'quit' :
                conns.remove(client_socket)
                break

            print('Received from ' + addr[0],':',addr[1],data.decode())

            sendmsg = "클라이언트 메세지: " + str(data.decode())

            for conn in conns :
                conn.send(sendmsg.encode('utf-8'))

        except Exception:
            print('Disconnected by ' + addr[0],':',addr[1])
            conns.remove(client_socket)
            break
    client_socket.close()
            
def main() :
    host = '127.0.0.1'
    port = 4400
    th = []
    
    #IPv4 체계, TCP 타입 소켓 객체를 생성(소켓타입)
    #SOCK_STREAM : 연결 지향형 소켓(TCP)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.timeout(1)
    #ip주소와 port번호를 함께 socket에 바인드한다.(주소 정보를 할당)
    #소켓에 포트번호를 부여
    #포트의 범위는 1~65535 사이의 숫자를 사용할 수 있음
    server_socket.bind((host, port))
    
    #연결 요청 대기 
    server_socket.listen(5)
    
    print('서버 시작')
    
    send = threading.Thread(target =sendMessage, args = ())
    send.start()
    while True :
        print('연결 대기중')
        try :
            # 연결 요청 대기중인 소켓에 대해 연경을 승낙하고 연결이 성립된 소켓과 주소정보를 반환
            client_socket, addr = server_socket.accept()
            conns.append(client_socket)
            client = threading.Thread(target=to_client, args=(client_socket,addr))
            client.start()
            th.append(client)
        except :
            server_socket.close()
            print('keyboard error')
            break
    
    for t in th:
        t.join()
    send.join()
    client_socket.close()
    server_socket.close()
 
if __name__ == '__main__' :
    main()
