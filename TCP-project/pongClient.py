from tkinter import *
from Pong import Ball, Player
import socket
import threading
import pickle

port = 5555 #  Send to port above 1024

#host = '10.18.101.97'
host = '127.0.0.1'

master = Tk()
w, h = 800, 600
update_time = 2
master.geometry(f'{w}x{h}')
canvas = Canvas(master, width=w, height=h)
canvas.place(x=0, y=0)
ball = Ball(w, h, canvas)
player1 = Player(0, 0, w, h, canvas)
player2 = Player(w-10, 0, w, h, canvas)
gameState = "PAUSE"
server = None

def key(event):
    k = event.char
    if k == 'w':
        player2.move(0, -1)
    elif k == 's':
        player2.move(0, 1)

def draw():
    global gameState
    global player1, player2, master, canvas, ball
    canvas.delete("all")
    player1.display()
    player2.display()
    ball.display()

def update():
    global gameState, master, server
    if server is not None:
        global player2
        player2.update()
        draw()
        sendPosition(server, player2)
    else:
        canvas.create_text(w//3, h//3, text= "Connecting to server")
    master.after(update_time, update)

def sendPosition(server, player2):
    pX, pY = player2.position
    msg = pickle.dumps((pX, pY))
    server.sendall(msg)

master.bind("<Key>", key)
def getConnection():
    global server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        port = 5556
        s.connect( (host, port))
        server = s
        while True:
            try: 
                msg = s.recv(1024)
                if not msg:
                    print("Server disconnect")
                    break
                (bx, by, px, py) = pickle.loads(msg)
                ball.setPosition(bx, by)
                player1.setPosition(px, py)
            except Exception as e:
                print(e)

threading.Thread(target=getConnection).start()
master.after(update_time, update)
master.mainloop()


