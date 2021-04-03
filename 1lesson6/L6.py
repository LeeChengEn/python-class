from pycat.window import Window
from pycat.sprite import Sprite
from pycat.scheduler import Scheduler
from pyglet.image import create
from pyglet.window.key import DELETE

window=Window(background_image="underwater_04.png")


class Spaceship(Sprite):

    def on_create(self):
        self.image="saucer.png"
        self.scale=0.35
        self.y=500
        self.score=0
        self.add_tag('spaceship')
       

    def on_update(self, dt):
        self.move_forward(10)
        if self.touching_window_edge():
            self.rotation +=180

s=window.create_sprite(Spaceship)


class Alien(Sprite):

    def on_create(self):
        self.image="1.png"
        self.scale=0.25
        self.goto_random_position()
        self.y=70
        self.is_moving_up=False
        
    def on_update(self, dt):
        if self.is_moving_up==True:
           self.y +=10

        if self.touching_window_edge():
            self.delete()

        if self.touching_any_sprite_with_tag('spaceship'):
            s.score +=1
            print(s.score)
            self.delete()

    def on_left_click(self):
        self.is_moving_up=True


def my_alien(dt):
    window.create_sprite(Alien)
    
Scheduler.update(my_alien, delay=1)


window.run()