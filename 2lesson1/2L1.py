from pycat.core import Window ,Sprite , KeyCode ,Scheduler ,Label
from pycat.label import Label
import random

window = Window(enforce_window_limits=False)

class Player(Sprite):

    def on_create(self):
        self.image = "bird.gif"
        self.y = window.height/2
        self.x = 100
        self.scale = 0.3

    def on_update(self, dt):
        self.y -= 1.5
        if window.is_key_down(KeyCode.SPACE):
            self.y += 40

window.create_sprite(Player)

class Pipe(Sprite):

    def on_create(self):
        self.image = "pipe.png"
        self.scale = 0.7
        self.x = window.width + self.width/2

    def on_update(self, dt):
        self.x -= 4
        if self.x < -self.width/2:
            self.delete()
        
def makes_pipe ():
    bottom_pipe = window.create_sprite(Pipe)
    top_pipe = window.create_sprite(Pipe)
    top_pipe.y = window.height
    top_pipe.rotation += 180
    a = int(bottom_pipe.height/2)
    offset = random.randint(-a,a)
    bottom_pipe.y += offset
    top_pipe.y += offset                     


class Score(Label):
    def on_create(self):
       self.text = "score"
    

Scheduler.update(makes_pipe ,1.6)
window.create_sprite(Pipe)
window.create_label(Score)

window.run()