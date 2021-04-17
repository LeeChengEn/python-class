from pycat.core import Window as W
from pycat.sprite import Sprite
from typing import List
from random import randint
w = W()

class Turtle(Sprite):
    def draw_forward(self, distance):
        prevx = self.x
        prevy = self.y
        self.move_forward(distance)
        w.create_line(prevx, prevy, self.x, self.y)
    
    def draw_rect(self, width, height):
        self.draw_forward(width)
        self.rotation += 90
        self.draw_forward(height)
        self.rotation += 90
        self.draw_forward(width)
        self.rotation += 90
        self.draw_forward(height)
        self.rotation += 90

class Building():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.window:List[Window] = []
        x = self.x + self.width/3
        x2 = self.x + 2*self.width/3
        for i in range(self.height//50):
            y = self.y + i*40 + 60
            self.window.append(Window(x,y,20,20))
            self.window.append(Window(x2,y,20,20))

    def draw(self, t:Turtle):
        t.rotation = 0
        t.x = self.x
        t.y = self.y
        t.draw_rect(self.width, self.height)
        for w in self.window:
            w.draw(t)

    
class Window():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self, t:Turtle):
        t.rotation = 0
        t.x = self.x
        t.y = self.y
        t.draw_rect(self.width, self.height)


turtle = w.create_sprite(Turtle)
for i in range(4):
    b = Building(i*300+30, 10, 250, randint(300,600))
    b.draw(turtle)
# win = Window(300, 10, 40, 70)
# win.draw(turtle)

# turtle.position = w.center
# for i in range(20):
#     turtle.draw_rect(100, 200)
#     turtle.rotation += 20

w.run()