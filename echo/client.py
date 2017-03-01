import socket
import time

port = 30555

client_socket = socket.socket()

client_socket.connect(('localhost', port))

while True:

    the_data = input("> ")

    the_data = bytes(the_data, encoding='utf-8')

    time_on_send = time.time()

    client_socket.send(the_data)
    data = client_socket.recv(512)

    time_on_receive = time.time()
    data = data.decode()
    split_list = data.split("?")
    time_on_server = float(split_list.pop())
    data = split_list.pop()

    overall_delta_time = (time_on_server - time_on_send) + (time_on_receive - time_on_server)
    print("Returned:", data)
    print("Client to server latency:", (time_on_server - time_on_send) * 1000, "ms")
    print("Server to client latency:", (time_on_receive - time_on_server) * 1000, "ms")
    print("Took", overall_delta_time * 1000, "ms")
client_socket.close()
