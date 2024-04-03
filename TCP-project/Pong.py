
class Ball():

    def __init__(self,w, h, canvas):
        self.position = (w//2, h//2)
        self.w = w
        self.h = h
        self.velocity = 0, 0
        self.canvas = canvas
        self.radius = 8
        self.speed = 0.5
    def display(self):
        x, y = self.position
        r = self.radius
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill="black")
    def update(self):
        x, y = self.position
        vx, vy = self.velocity
        x += vx * self.speed
        y += vy * self.speed
        if( x < 0 or x > self.w):
            self.start()
            return
        elif(y < 0 or y > self.h):
            vy *= -1

        self.velocity = vx, vy
        self.position =  x, y

    def start(self):
        self.velocity = -0.8, 0
        self.position = (self.w//2, self.h//2)


    def setPosition(self, x, y):
        self.position = x, y

    def bounce(self, x, y):
        vx, vy = self.velocity
        vx *= -1 * x
        vy *= -1 * y
        self.velocity = vx, vy


class Player():
    
    def __init__(self,x, y,  w, h, canvas):
        self.position = x, y
        self.w = w
        self.h = h
        self.velocityY = 0
        self.canvas = canvas
        self.size = 80
        self.speed = 0.5
        self.max = 2

    def display(self):
        self.canvas.create_rectangle(self.position[0], self.position[1], self.position[0] + 10, self.position[1] + self.size, fill="black")

    def update(self):
        x = self.position[0]
        y = self.position[1]
        vy = self.velocityY
        y += vy
        if (y < 0) :
            y = 0
        if  (y > self.h - self.size):
            y = self.h - self.size
        self.position = x, y
    
    def move(self, x, y):
        self.velocityY = self.speed * y

    def setPosition(self, x, y):
        self.position = x, y
    
    def hitBall(self, ball):
        px, py = self.position
        bx, by = ball.position
        if bx > px and bx < (px + 10) and by > py and by < (py + self.size):
            ball.bounce(1, 0)