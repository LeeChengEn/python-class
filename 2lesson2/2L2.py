import enum
from sys import platform
from pycat.base.color import Color
from pycat.base.event.mouse_event import MouseEvent
from pycat.core import Window ,Sprite
from pyglet.gl.glext_arb import PFNGLVERTEX4HVNVPROC

window = Window(background_image = "colorfulcity.png")
window.background_sprite.scale = 1.4

class Ghoststate(enum.Enum):
    WAIT_FOR_CLICK = enum.auto()
    JUMP = enum.auto()
    RESET = enum.auto()


class Player(Sprite):

    def on_create(self):
        self.image = "hedgehog-c.png"
        self.reset()
        self.add_tag("platform")

    def reset(self):
        self.position = (100,350)
        self.scale = 0.5
        self.rotation = 0
        self.x_speed = 0
        self.y_speed = 0
        self.state = Ghoststate.JUMP

    def on_update(self, dt):
        if self.state == Ghoststate.JUMP:
            self.x += self.x_speed
            self.y += self.y_speed
            self.y_speed -= 0.6

        if self.y_speed <= 0:
            for p in platforms:
                if self.y > p.y:
                    if self.is_touching_sprite(p.hitbox):
                        self.y = p.hitbox.y + p.hitbox.height/2 + self.height/2
                        self.state = Ghoststate.WAIT_FOR_CLICK
            
            if self.is_touching_window_edge():
                self.state = Ghoststate.RESET

            if self.is_touching_sprite(toad):
                self.state = Ghoststate.RESET

        if self.state == Ghoststate.RESET:
            self.scale *= 0.99
            self.rotation += 5
            if self.rotation > 180:
                self.reset()

    def on_click_anywhere(self, mouse_event: MouseEvent):
        if self.state == Ghoststate.WAIT_FOR_CLICK:
            x_dist = mouse_event.position.x - self.x
            y_dist = mouse_event.position.y - self.y

            self.x_speed = x_dist * 0.045
            self.y_speed = y_dist * 0.04
            self.state = Ghoststate.JUMP



class Platform(Sprite):

    def on_create(self):
        self.image = "rocks.png"
        self.x = 100
        self.y = 250
        self.add_tag("platform")

    def add_hitbox(self):
        self.hitbox = window.create_sprite()
        self.hitbox.position = self.position
        self.hitbox.height = 50
        self.hitbox.width = 0.5*self.width
        self.hitbox.color = Color.BLACK
        self.hitbox.opacity = 5

platforms = [
    window.create_sprite(Platform),
    window.create_sprite(Platform, x = 325, y = 400, scale = 0.7),
    window.create_sprite(Platform, x = 600, y = 150, scale = 0.9),
    window.create_sprite(Platform, x = 800, y = 300, scale = 0.9),
]

for p in platforms:
    p.add_hitbox()

window.create_sprite(Player)

class Ghost(Sprite):

    def on_create(self):
        self.image = "wizard-toad-b.png"
        self.scale = 1.3
        self.x = 1100
        self.y = 250

    def on_update(self, dt):
        pass

toad=window.create_sprite(Ghost)

window.run()