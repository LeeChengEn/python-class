from pycat.core import Window, Point, Sprite 
from math import sqrt

from pyglet import window

w = Window()

class Turtle(Sprite):
    def on_create(self):
        pass

    def draw_traingle(self,length):
        t_a = self.position
        self.move_forward(length)
        t_b = self.position
        self.rotation += 120
        self.move_forward(length)
        t_c = self.position
        self.move_forward(length)
        w.create_line(t_a.x, t_a.y, t_b.x, t_b.y)
        w.create_line(t_a.x, t_a.y, t_c.x, t_c.y)
        w.create_line(t_c.x, t_c.y, t_b.x, t_b.y)

turtle = w.create_sprite(Turtle)

for i in range(200):
    turtle.position = w.center
    turtle.draw_traingle(300)
    turtle.rotation += 7

w.run()