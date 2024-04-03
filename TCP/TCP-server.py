import socket

port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('127.0.0.1', port))
s.listen(10)

while True:
    print("Waiting for client...")
    client_socket, addr = s.accept()
    with client_socket:
        print(f"Connection from {addr}")
        while True:
            msg = client_socket.recv(1024)
            if not msg:
                print('Client disconnected')
                break
            msg = msg.decode('utf-8')
            print(f"Recieved message: {msg}")
            msg += ' haha!!!'
            client_socket.sendall(msg.encode('utf-8'))