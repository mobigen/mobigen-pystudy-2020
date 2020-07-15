import socket
import threading
import time
from collections import deque
 

class client(threading.Thread):
    def __init__(self, client_socket, addr, conns) :
        threading.Thread.__init__(self)
        self.conn = client_socket
        self.addr = addr
        self.conns = conns

    def run(self):
        print('%s에서 접속하였습니다.' % self.addr[1])
        check = '당신('+ str(self.addr[1]) +')은 무사히 서버에 접속했습니다.'
        self.conn.send(check.encode('utf-8'))
        while True :
            try :
                data = self.conn.recv(1024)
                if not data :
                    print('Disconnected' + self.addr[0],':',self.addr[1])
                    break

                print('Received from ' + self.addr[0],':', self.addr[1],data.decode())
                sendmsg = '클라이언트 ' +str(self.addr[1])+'의 메세지 : '+str(data.decode())

                for conn in self.conns :
                    conn.send(sendmsg.encode('utf-8'))

            except Exception :
                print('Disconnected by ' + self.addr[0],':', self.addr[1])
                self.conns.remove(self.conn)
                break
        
        self.conn.close()

            
def main() :
    host = '127.0.0.1'
    port = 4400
    conns = []
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
    
    while True :
        print('연결 대기중')
        try :
            # 연결 요청 대기중인 소켓에 대해 연경을 승낙하고 연결이 성립된 소켓과 주소정보를 반환
            client_socket, addr = server_socket.accept()
            conns.append(client_socket)
            cli = client(client_socket,addr, conns)
            cli.start()
            th.append(cli)
        except :
            server_socket.close()
            print('keyboard error')
            break
    
    for t in th:
        t.join()

    client_socket.close()
    server_socket.close()
 
if __name__ == '__main__' :
    main()
