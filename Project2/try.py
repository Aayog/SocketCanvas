from tkinter import *
import pickle

class Paint:
    def __init__(self):
        master = Tk()
        master.geometry('800x600')
        w, h = 600, 600

        myCanvas = Canvas(master, width=w, height=h)
        myCanvas.place(x=0, y=0)
        myCanvas.configure(bg="white")

        prevX, prevY = -99, -99 
        points = []

        penColor = 'black'
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
        clearButton = Button(master, text="CLEAR", width=5,height=5)
        clearButton.place(x=w+a, y=b)
        clearButton.bind('<Button>', clearAll)
        prevX2, prevY2 = -99, -99 
    
    def changeColor(self, event=None):
        self.penColor = event.widget.color

    
    def clearAll(self, event=None):
        self.points = []
        self.myCanvas.delete("all")
        
    

    def getPoints(self):
        while True:
            (msg,self.client_addr) = s.recvfrom(1024)

            try: 
                (x, y,penColor) = pickle.loads(msg)
                
                self.trigger(x,y,penColor)
            except Exception as e:
                print(e)
                next


  

    def trigger(self, x, y,penColor):
        global prevX2, prevY2
        if (prevX2 == -99):
            prevX2, prevY2 = x, y
        myCanvas.create_line(prevX2, prevY2, x, y, fill=penColor)
        prevX2, prevY2 = x, y
            
    def paint(self, event):
        global prevX, prevY, points
        x, y = event.x, event.y
        if (prevX == -99):
            prevX, prevY = x, y
        myCanvas.create_line(prevX, prevY, x, y, fill=penColor)
        #points.append((x, y, penColor))
        prevX, prevY = x, y
        msg = pickle.dumps(( x,y, penColor))
        s.sendto(msg, (server_ip, port_number))
