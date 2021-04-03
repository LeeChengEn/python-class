from re import match
from pycat.window import Window
from pycat.sprite import Sprite
from pyglet import window
from pyglet.window.key import W
from pycat.core import Player, AudioLoop
import random
select_sprite_sound = Player('hit.wav')
match_sprite_sound = Player('point.wav')
no_match_sprite_sound = Player('laugh.wav')
audio_loop = AudioLoop('LoopLivi.wav', volume=0.2)
audio_loop.play()

w=Window(background_image="forest_04.png",draw_sprite_rects=True )

click_sprite=[]

class Card(Sprite):

    def on_create(self):
        self.is_visible=False
        self.is_rotating=False

    def on_update(self,dt):
        if self.is_rotating:
            self.rotation+=2
            if self.rotation>120:
                self.delete()
            

    def on_left_click(self):
        if self not in click_sprite:

            if len(click_sprite)<2:
                select_sprite_sound.play()
                click_sprite.append(self)
                self.is_visible=True
        

w.create_sprite(Card)

# w.create_sprite(Card, x=100, y=100, image="avatar_01.png")
# w.create_sprite(Card, x=100, y=300, image="avatar_01.png")
# w.create_sprite(Card, x=200, y=300, image="avatar_02.png")
# w.create_sprite(Card, x=300, y=200, image="avatar_02.png")
# w.create_sprite(Card, x=200, y=200, image="avatar_03.png")
# w.create_sprite(Card, x=300, y=100, image="avatar_03.png")
# w.create_sprite(Card, x=100, y=200, image="avatar_04.png")
# w.create_sprite(Card, x=200, y=100, image="avatar_04.png")

class Checkbutton(Sprite):

    def on_create(self):
        self.image="button.png"
        self.x=600
        self.y=100
        self.scale=0.4

    def on_left_click(self):
        if len(click_sprite)==2:
            sprite1:Card=click_sprite[0]
            sprite2:Card=click_sprite[1]
        
            if sprite1.image==sprite2.image:
                match_sprite_sound.play()
                sprite1.is_rotating=True
                sprite2.is_rotating=True

            else:
                no_match_sprite_sound.play()
                sprite1.is_visible=False
                sprite2.is_visible=False
            
            click_sprite.clear()

w.create_sprite(Checkbutton)

avatars=4*["avatar_01.png","avatar_02.png","avatar_03.png","avatar_04.png"]
random.shuffle(avatars)
for x in range(100,500,100):
    for y in range(100,500,100):
        w.create_sprite(Card,x=x,y=y,image=avatars.pop())

w.run()