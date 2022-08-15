import socket

HOST = ""
PORT = 7000

server_addr = (HOST, PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    outdata = input()
    s.sendto(outdata.encode(), server_addr)

    data, addr = s.recvfrom(1024)
    print(data)