from pycat.window import Window
from pycat.sprite import Sprite
from pycat.keyboard import KeyCode
from pycat.scheduler import Scheduler
from pycat.collision import is_aabb_collision
import random

w  = Window(background_image="img/beach_03.png")


class Player(Sprite):

    def on_create(self):
        self.image="img/cat.png"
        self.x=500
        self.y=100
        self.name = "scratch"
        self.points = 0

    def on_update(self, dt):

        if w.get_key(KeyCode.RIGHT):
            self.scale_x=+1
            self.x +=10
           

        if w.get_key(KeyCode.LEFT):
            self.scale_x=-1
            self.x -=10
        
       


           
p=w.create_sprite(Player)


class Diamand(Sprite):

    def on_create(self):
       
        self.image="img/gem_shiny01.png"
        self.goto_random_position()
        self.y=700
        self.scale=0.25

    def on_update(self, dt):

        if is_aabb_collision(p, self):
            p.points +=1
            print(p.points)
            self.delete()

        if self.y<1:
            self.delete()
        
        self.y -=10



        

f=["img/gem_shiny01.png","img/gem_shiny02.png","img/gem_shiny03.png","img/gem_shiny04.png","img/gem_shiny05.png"]
def creatediamand(dt):
    s = w.create_sprite(Diamand)
    s.image=random.choice(f)


Scheduler.update(creatediamand, delay=.02)




w.run()