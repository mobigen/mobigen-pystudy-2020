#!/usr/bin/python3

import threading
import time
import random
from collections import deque
from queue import Queue


class Consumer(threading.Thread): 
    
    def __init__(self,name,q):
        
        threading.Thread.__init__(self)
        self.name = name
        self.q = q
       
    def run(self):                                                                   
        for i in range(5):                                                           
            # queue 에서 뽑아먹는다                                                   
            print('[%s] gets %s'%(self.name, self.q.popleft()))
            time.sleep(0.0)                                                          
    #def __del__(self,):



class Producer(threading.Thread):

    def __init__(self,name,q):
        
        threading.Thread.__init__(self)
        self.name = name
        self.q = q
     

    def run(self):
        for i in range(10):
            # 0~20 사이의 임의의 난수를 queuqe 에 밀어 넣음
            randomInt = random.randint(0,20)
            self.q.append(randomInt)
            print('[%s] puts %s -----------------' % (self.getName(),randomInt))
            time.sleep(0.0)


def main():
    # 소비자 10
    COUNSUMER_COUNT = 10
    # 생산자 5
    PRODUCER_COUNT = COUNSUMER_COUNT


    # 저장공간이 10인 queue 생성
    q = deque([])
    

    #thread 리스트
    con = []
    pro = []

    #Consumer thread 생성
    for i in range(COUNSUMER_COUNT):
        con.append(Consumer(i,q))

    # Producer thread 생성
    for i in range(PRODUCER_COUNT):
        pro.append(Producer(i,q))

    # Consumer 먼저 시작
    for th in con:
        th.start()

    # Producer 시작
    for th in pro:
        th.start()

    # thread 종료까지 대기
    for th in con:
        th.join()

    for th in pro:
        th.join()

    print('Exiting')

if __name__ == "__main__" :

    main()



#queue를 이용한 multi thread 생산자-소비자 모델
#        - 경쟁적으로 queue에 마구 넣고, 마구 뽑지만 deadlock이나 충돌같은 건 발생하지 않음.
#         thread 내에서 lock을 걸고 할 필요가 없으므로 상대적으로 깔끔한 코드가 나옵니다.
