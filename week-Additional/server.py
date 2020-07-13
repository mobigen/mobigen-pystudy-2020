import socket
import select

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234

#서버 소켓 생성#####################################################

# socket.AF_INET - address family, IPv4
# socket.SOCK_STREAM - TCP, UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind, 서버가 os에게 ip, port를 사용하겠다고 알림
server_socket.bind((IP, PORT))

# 서버가 새로운 커넥션을 기다림
server_socket.listen()

# 소켓 리스트 - 서버 소켓을 미리 소켓 리스트에 넣어둠
sockets_list = [server_socket]

# 접속된 클라이언트 리스트
clients = {}

print('connections on {IP}:{PORT}...')

def receive_message(client_socket):

    try:

        message_header = client_socket.recv(HEADER_LENGTH)

        # 클라이언트에서 보내는 데이터가 없을 경우 해당 클라이언트 소켓을 닫는다.
        if not len(message_header):
            return False

        # 헤더를 int 값으로 변경 == 메세지 크기
        message_length = int(message_header.decode('utf-8').strip())

        # 메세지 헤더와 메세지 데이터를 리턴
        return {'header': message_header, 'data': client_socket.recv(message_length)}

    except:
        #갑작스럽게 클라이언트가 접속을 끊을때
        return False

while True:

    # select 함수
    #   - rlist - 데이터를 받을 소켓 리스트
    #   - wlist - 데이터를 전송할 소켓 리스트 
    #   - xlist - 에러를 모니터링해야하는 소켓 리스트

    # 반환 lists:
    #   - reading - 데이터를 읽을 소켓 
    #   - writing - 데이터를 쓸 소켓
    #   - errors  - 에러를 모니터링할 소켓들
    # select은 데이터를 전송받을때까지 기다린다.
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets:

        # 소켓이 서버 소켓인 경우
        if notified_socket == server_socket:
           
            #새로운 커넥션이 들어올때까지 기다림
            client_socket, client_address = server_socket.accept()

            #클라이언트로부터 값을 받음
            user = receive_message(client_socket)

            #클라이언트가 갑자기 접속을 끊었을때
            if user is False:
                continue

            # 수락된(accept)된 소켓을 select.select() 리스트에 추가
            sockets_list.append(client_socket)

            # 사용자 이름과 헤더를 추가
            clients[client_socket] = user

            print('접속자 {}:{}, username: {}'.format(*client_address, user['data'].decode('utf-8')))

        # 소켓이 클라이언트 소켓인 경우
        else:

            # 전송된 메세지
            message = receive_message(notified_socket)

            # 클라이언트 접속 끊김
            if message is False:
                print('접속 끊김: {}'.format(clients[notified_socket]['data'].decode('utf-8')))

                # 소켓리스트에서 제외
                sockets_list.remove(notified_socket)

                # 클라이언트 리스트에서 제외
                del clients[notified_socket]

                continue

            # 메세지를 보낼 소켓 리스트
            user = clients[notified_socket]

            print(f'전달된 메세지 {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')

            # 메세지 전체 소켓으로 전달(broadcast)
            for client_socket in clients:
                #전송한 사람이 자기 자신이 아닐때
                if client_socket != notified_socket:
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

    # 에러가 발생된 경우
    for notified_socket in exception_sockets:

        # 에러가 발생된 경우 소켓 리스트에서 제외
        sockets_list.remove(notified_socket)

        # 소켓리스트에서 제외
        del clients[notified_socket]