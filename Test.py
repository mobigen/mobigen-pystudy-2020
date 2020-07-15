import threading
import time


def testfunc(conns) :
    print('thread start')
    while True :
        for conn in conns :
            print(conn)
        time.sleep(10)

def main() :
    conns = [1,2,3]

    t = threading.Thread(target=testfunc, args=(conns,))
    t.start()

    conns.append(4)

    t.join()



if __name__ == '__main__' :
    main()