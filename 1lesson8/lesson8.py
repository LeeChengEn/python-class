from pycat.window import Window
from pycat.sprite import Sprite
from pyglet.window.key import W

w=Window(background_image="forest_04.png",draw_sprite_rects=True )

click_sprite=[]

class Card(Sprite):

    def on_create(self):
        self.is_visible=False

    def on_left_click(self):
         if self not in click_sprite:
            if len(click_sprite)<2:
                click_sprite.append(self)
                self.is_visible=True
        
        
w.create_sprite(Card)

w.create_sprite(Card, x=100, y=100, image="avatar_01.png")
w.create_sprite(Card, x=100, y=200, image="avatar_01.png")
w.create_sprite(Card, x=200, y=100, image="avatar_02.png")
w.create_sprite(Card, x=200, y=200, image="avatar_02.png")

class Checkbutton(Sprite):

    def on_create(self):
        self.image="button.png"
        self.x=450
        self.y=100
        self.scale=0.4

    def on_left_click(self):
        if len(click_sprite)==2:
            sprite1:Sprite =click_sprite[0]
            sprite2:Sprite =click_sprite[1]
        
            if sprite1.image==sprite2.image:
                sprite1.delete()
                sprite2.delete()
            else:
                sprite1.is_visible=False
                sprite2.is_visible=False
            click_sprite.clear()




w.create_sprite(Checkbutton)

w.run()