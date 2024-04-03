#Name: Alex Scull, Aayog Koirala, Miles Furr
#Date: Februrary 20th, 2020
#Description: Server Side for a Common canvas app

from tkinter import *
from tkinter import messagebox
import socket
import pickle
import threading

port_number = 5555
server_ip ="127.0.0.1"

master = Tk()
master.geometry('800x600')
w, h = 600, 600

myCanvas = Canvas(master, width=w, height=h)
myCanvas.place(x=0, y=0)
myCanvas.configure(bg="white")

prevX, prevY = -99, -99 
points = []
client_addr = None

penColor = 'black'

# Color pallet
def changeColor(event=None):
    global penColor
    penColor = event.widget.color

# Different buttons for the color pallet 
a, b = 0, 0
for i in ["black", "white", "red", "blue", "green", "yellow", "purple", "brown"]:
    button = Button(master, width=5, height=5, bg=i)
    button.place(x=w+a, y=0+b)
    button.bind('<Button>', changeColor)
    button.color = i
    a+=50
    if(a >= 100):
        a %= 50
        b+=100

# Callback for the clear button
def clearAll(event=None):
    global myCanvas, points
    points = []
    myCanvas.delete("all")

clearButton = Button(master, text="CLEAR", width=5,height=5)
clearButton.place(x=w+a, y=b)
clearButton.bind('<Button>', clearAll)

prevX2, prevY2 = -99, -99 
# Called after points recieved from the client to draw on the canvas
def trigger(x, y,penColor):
    global prevX2, prevY2
    if (prevX2 == -99):
        prevX2, prevY2 = x, y
    myCanvas.create_line(prevX2, prevY2, x, y, fill=penColor)
    prevX2, prevY2 = x, y
     
# sending the points to draw to the server
def sendPoints(x,y,penColor):
	global client_addr

	if client_addr is not None:
		msg = pickle.dumps((x,y,penColor))
		s.sendto(msg, (client_addr))


# Callback when the mouse is clicked, to draw on the canvas
def paint(event):
    global prevX, prevY, points, client_addr
    x, y = event.x, event.y
    if client_addr is None:
        messagebox.showwarning(title="Client error", message="No client connected")
    if (prevX == -99):
        prevX, prevY = x, y
    myCanvas.create_line(prevX, prevY, x, y, fill=penColor)
    points.append((x, y, penColor))
    prevX, prevY = x, y
    sendPoints(x,y, penColor)
    
# B1-Motion binds the left-click of the mouse and it's movement to paint() 
myCanvas.bind('<B1-Motion>', paint)

# Socket declaration and setting it to UDP server in the localhost
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((server_ip, port_number))

# Getting points from the client to draw on the canvas
def getPoints():
	global client_addr, s
	while True:
		(msg,client_addr) = s.recvfrom(1024)

		try: 
			(x, y, penColor) = pickle.loads(msg)
			
			trigger(x,y,penColor)
		except Exception as e:
			print(e)
			next	

# A separate thread to wait to recieve points from the client
threading.Thread(target=getPoints).start()
master.title("Canvas Server")
master.mainloop()

