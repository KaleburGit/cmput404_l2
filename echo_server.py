import socket
from threading import Thread

BYTES_TO_READ = 4096
HOST = "127.0.0.1" #loop back address, just means local
PORT = 8080

def handle_connection(conn, addr):
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(BYTES_TO_READ)
            if not data:
                break
            print(data)
            conn.sendall(data) #send it back to client

#start single threaded echo server
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #uses the same bind port. set reuseADDR to 1
        s.listen()
        conn, addr = s.accept() # conn = socket referring to the client
        handle_connection(conn, addr) # send it a response

def start_threaded_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.listen(2)
        while True:
            conn, addr = s.accept() # conn = socket referring to the client
            thread = Thread(target=handle_connection, args=(conn, addr)) # send it a response
            thread.run()

#start_server()
start_threaded_server()

