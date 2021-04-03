from pycat.base.color import Color
from pycat.core import KeyCode, Sprite, Window, Label
from pyglet.image import create
from pyglet.window.key import W
w = Window(background_image = "beach.jpg")

w.create_label()

class PlayerOneScore(Label):
    def on_create(self):
        self.score = 0
        self.text = "player one score: " + str(self.score)
        self.x = 150
        self.y = 600
        self.font_size = 30
        self.color = Color.CHARTREUSE
        self.font = 'Comic Sans MS'

    def update_label(self):
        self.text = "player one score: " + str(self.score)
    
    def on_update(self, dt: float):
        if player_two_score.score>=3:
            self.text = "you lose "
            self.x = 150
            self.y = 600
            self.font_size = 50
            self.color = Color.RED
            self.font = 'Comic Sans MS'
            game_over()

player_one_score = w.create_label(PlayerOneScore)



class PlayerTwoScore(Label):
    def on_create(self):
        self.score = 0
        self.text = "player two score: " + str(self.score)
        self.x = 850
        self.y = 600
        self.font_size = 30
        self.color = Color.CHARTREUSE
        self.font = 'Comic Sans MS'

    def update_label(self):
        self.text = "player one score: " + str(self.score)
    
    def on_update(self, dt: float):
        if player_one_score.score>=3:
            self.text = "you lose "
            self.x = 850
            self.y = 600
            self.font_size = 50
            self.color = Color.RED
            self.font = 'Comic Sans MS'
            game_over()

player_two_score = w.create_label(PlayerTwoScore)



class GameOver(Label):
    def on_create(self):
        pass

    def on_update(self, dt: float):
        if player_one_score.score>=3:
            self.text = "Game Over " 
            self.x = 300
            self.y = 400
            self.font_size = 100
            self.color = Color.RED
            self.font = 'Comic Sans MS'
        if player_two_score.score>=3:
            self.text = "Game Over " 
            self.x = 300
            self.y = 400
            self.font_size = 100
            self.color = Color.RED
            self.font = 'Comic Sans MS'
    
game_over=w.create_label(GameOver)



class Net(Sprite):

    def on_create(self):
        self.image = "net.png"
        self.x = 650
        self.y = 100

    def on_update(self, dt):
        pass

net = w.create_sprite(Net)



class PlayerOne(Sprite):

    def on_create(self):
        self.image = "gobo-b r.png"
        self.x = 300
        self.y = 100
        self.scale = 0.7
        self.y_speed = 0
        self.score = 0

    def on_update(self, dt):
        if w.get_key_down(KeyCode.W):
            self.y_speed = 15
        else:
            self.y_speed -= 0.4
            self.y += self.y_speed
        if self.y<100:
            self.y_speed = 0
            self.y = 100
        if w.get_key(KeyCode.A):
            self.x -= 9
        if w.get_key(KeyCode.D):
            self.x += 9
        if self.touching_sprite(net):
            self.x_speed = 0
            self.x -= 9
        if self.x>590:
            self.x_speed = 0
            self.x -= 9
        
player_one = w.create_sprite(PlayerOne)



class PlayerTwo(Sprite):

    def on_create(self):
        self.image = "gobo-b.png"
        self.x = 960
        self.y = 100
        self.scale = 0.7
        self.y_speed = 0
        self.score = 0


    def on_update(self, dt):
        if w.get_key_down(KeyCode.UP):
            self.y_speed = 15
        else:
            self.y_speed -= 0.4
            self.y += self.y_speed
        if self.y<100:
            self.y_speed = 0
            self.y = 100
        if w.get_key(KeyCode.LEFT):
            self.x -= 9
        if w.get_key(KeyCode.RIGHT):
            self.x += 9
        if self.x<725:
            self.x_speed = 0
            self.x += 9
          
player_two=w.create_sprite(PlayerTwo)



class Ball(Sprite):

    def on_create(self):
        self.image = "beachball.png"
        self.x = 650
        self.y = 400
        self.scale = 0.7
        self.y_speed = 0
        self.x_speed = 0
        self.goto(player_one)
        self.is_in_play = True
        self.lastplayer = player_one
    def on_update(self, dt):
        if self.touching_sprite(player_one):
            self.y_speed = 17.5
            self.x_speed = 15.5
            self.lastplayer = player_one
        elif self.touching_sprite(player_two):
            self.y_speed = 17.5
            self.x_speed = -15.5
            self.lastplayer = player_two
        elif self.y < 20:
            self.x_speed = 0
            self.y_speed = 0
            # add pause here
            if self.x < net.x:
                player_two.x = 960
                self.goto(player_two)
                player_two_score.score += 1
                player_two_score.update_label()
            else:
                player_one.x = 300
                self.goto(player_one)
                player_one_score.score += 1
                player_one_score.update_label()
        else:
            self.y_speed -= 0.3
        self.x += self.x_speed
        self.y += self.y_speed

        if self.touching_sprite(net):
            self.x_speed *= -1
            self.is_in_play = False
        # if self.touching_window_edge() and self.is_in_play==False:
        #     self.goto(playertwo)
        # if self.y<0 and self.is_in_play==False:
        #     self.goto(playertwo)
        if self.x<0:
            self.x_speed *= -1
        if self.x>w.width:
            self.x_speed *= -1
        if self.y>w.height:
            self.y_speed *= -1
  
ball = w.create_sprite(Ball)



def game_over():
    ball.delete()
    player_one.delete()
    player_two.delete()
    net.delete()


w.run()