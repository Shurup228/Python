import socket
import time

port = 30555

a = socket.socket()
a.bind(('localhost', port))
print("Listening on port", port, "\n")
a.listen(2)
conn, addr = a.accept()
print(addr, "connected")

isBroken = False

while True:

    if isBroken:
        conn, addr = a.accept()
        print(addr, "connected")
        isBroken = False

    data = conn.recv(512)
    print("Got data: ", data)

    if data:
        time_on_server = time.time()

    data = data + b'\n' + b'?' + bytes(str(time_on_server), encoding='utf-8')
    try:
        conn.send(data)
        print("Returning data to client", addr)
    except BrokenPipeError:
        print("\n***Lost connection to", addr, "disconnecting...***\n")
        conn.detach()
        isBroken = True


conn.close()