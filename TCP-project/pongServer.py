from tkinter import *
from Pong import Ball, Player
import socket
import threading
import pickle

port = 5556 #  Send to port above 1024

host = socket.gethostname()
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

def initGame():
    global canvas, player1, player2, ball

def start():
    global ball 
    print("Starting")
    ball.start()
    print(ball.position)

def key(event):
    k = event.char
    if k == 'w':
        player1.move(0, -1)
    elif k == 's':
        player1.move(0, 1)
def space(event):
    global gameState
    if gameState == "PAUSE":
        gameState = "START"
        start()   
def draw():
    global gameState
    if gameState == "START":
        global player1, player2, master, canvas, ball
        canvas.delete("all")
        player1.display()
        player2.display()
        ball.display()

def update():
    global gameState, master, client
    if gameState == "START" and client is not None:
        global player1, ball
        player1.update()
        player1.hitBall(ball)
        player2.hitBall(ball)
        ball.update()
        draw()
        sendPosition(client, ball, player1)
    else:
        canvas.create_text(w//2, h//2, text= "PRESS SPACE TO START")
    master.after(update_time, update)

def sendPosition(client, ball, player1):
    bX, bY = ball.position
    pX, pY = player1.position
    msg = pickle.dumps((bX, bY, pX, pY))
    client.sendall(msg)

master.bind("<Key>", key)
master.bind("<space>", space)
client = None
def getConnection():
    global client
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        port = 5556
        s.bind( ('127.0.0.1', port) )
        s.listen()
        client_socket, addr = s.accept()
        client = client_socket
        while True:
            try: 
                msg = client_socket.recv(1024)
                if not msg:
                    print("Client disconnect")
                    break
                (playerX, playerY) = pickle.loads(msg)
                player2.setPosition(playerX, playerY)
            except Exception as e:
                print(e)

initGame()
threading.Thread(target=getConnection).start()
master.after(update_time, update)
master.mainloop()


