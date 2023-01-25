import socket
import _thread

server=""
port = 5555


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for Connection. \n Server Started")

def threaded_client(conn):
    pass

while True:
    conn, addr = s.accept()
    print(f"Connected to {addr}")

    start_new_thread 