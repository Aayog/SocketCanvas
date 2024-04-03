import socket

port = 5556
host = socket.gethostname()
host = '10.18.101.97'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    
    while True:
        message = input("What do you want to send?")

        s.sendall(message.encode('utf-8'))
        print("Message Sent!")
        rcv = s.recv(1024)
        print(f"Got: {rcv.decode('utf-8')}")
