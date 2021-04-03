from pycat.base.base_sprite import RotationMode
from pycat.core import Sprite, Window
import random


class Particle(Sprite):

    def on_create(self):
        self.add_tag('particle')
        self.goto_random_position()
        self.rotation = random.randint(0, 360)
        self.scale = 5
    def on_update(self,dt):
        self.move_forward(5)
        if self.touching_window_edge():
            self.rotation +=180
        
class ColorButton(Sprite):

    def on_left_click(self):
        for particle in window.get_sprites_with_tag('particle'):
            particle.color = self.color
window=Window()
window.create_sprite(ColorButton,x=100,y=100,scale=50,color=(0,255,0))
window.create_sprite(ColorButton,x=200,y=100,scale=50,color=(0,0,255))

class Createbutton(Sprite):
    def on_left_click(self):
        for _ in range(100):
            window.create_sprite(Particle)
window.create_sprite(Createbutton,x=300,y=100,scale=50,color=(255,0,0))

class Deletebutton(Sprite):
    def on_left_click(self):
        window.delete_sprites_with_tag('particle')
window.create_sprite(Deletebutton,x=400,y=100,scale=50,color=(100,100,0))


for _ in range(100):
    window.create_sprite(Particle)

window.run()