from socket import *
import time


def bench(addr, mes):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(addr)
    start = time.time()
    for _ in range(mes):
        sock.send(b'x')
        resp = sock.recv(10000)
    end = time.time()
    print(mes/(end - start), 'mes/sec')


if __name__ == '__main__':
    bench(('localhost', 30555), 1000000)
