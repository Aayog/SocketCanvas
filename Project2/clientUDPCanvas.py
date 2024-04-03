#Name: Alex Scull, Aayog Koirala, Miles Furr
#Date: Februrary 20th, 2020
#Description: Client Side for a Common canvas app

from tkinter import *
import socket
import pickle
import threading

port_number = 5555
server_ip ="127.0.0.1"
# UDP client
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

master = Tk()
master.geometry('800x600')
w, h = 600, 600

myCanvas = Canvas(master, width=w, height=h)
# "place" places the canvas exactly at 0, 0 ..regardless of the size of the canvas
myCanvas.place(x=0, y=0)
myCanvas.configure(bg="white")

# before starting the previous points set to an arbitrary value
prevX, prevY = -99, -99 

# default color set to black and the variable used to change based on the color pallet
penColor = 'black'

def changeColor(event=None):
    global penColor
    penColor = event.widget.color

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

def clearAll(event=None):
    global myCanvas, points
    points = []
    myCanvas.delete("all")
    
clearButton = Button(master, text="CLEAR", width=5,height=5)
clearButton.place(x=w+a, y=b)
clearButton.bind('<Button>', clearAll)

def getPoints():
	global s
	while True:
		(msg, client_addr) = s.recvfrom(1024)

		try: 
			(x, y,penColor) = pickle.loads(msg)
			
			trigger(x,y,penColor)
		except Exception as e:
			print(e)
			next


prevX2, prevY2 = -99, -99 

# Called after points recieved from the server to draw on the canvas
def trigger(x, y,penColor):
    global prevX2, prevY2
    if (prevX2 == -99):
        prevX2, prevY2 = x, y
    myCanvas.create_line(prevX2, prevY2, x, y, fill=penColor)
    prevX2, prevY2 = x, y
        
def paint(event):
    global prevX, prevY, points
    x, y = event.x, event.y
    if (prevX == -99):
        prevX, prevY = x, y
    myCanvas.create_line(prevX, prevY, x, y, fill=penColor)
    prevX, prevY = x, y
    msg = pickle.dumps(( x,y, penColor))
    s.sendto(msg, (server_ip, port_number))
    
threading.Thread(target=getPoints).start()
myCanvas.bind('<B1-Motion>', paint)
master.title("Canvas Client")
master.mainloop()

