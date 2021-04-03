from pycat.core import Color, KeyCode, Scheduler, Sprite, Window
import random
from pyglet.image import create

window = Window()

class Player(Sprite):

    def on_create(self):
        self.color = Color.AMBER
        self.scale = 33
        self.speed = 10

    def on_update(self, dt):
        if window.get_key(KeyCode.W):
            self.y += self.speed
        if window.get_key(KeyCode.A):
            self.x -= self.speed
        if window.get_key(KeyCode.S):
            self.y -= self.speed
        if window.get_key(KeyCode.D):
            self.x += self.speed
        # fill in code for keys A, S, D

    def on_left_click_anywhere(self):
        window.create_sprite(Bullet)
    
player = window.create_sprite(Player)

class Bullet(Sprite):

    def on_create(self):
        self.scale = 13
        self.color = Color.AZURE
        self.speed = 6
        self.position = player.position

    def on_update(self, dt):
        self.point_toward_mouse_cursor()
        self.move_forward(self.speed)
        self.add_tag('bullet')
        if self.touching_window_edge():
            self.delete()


class Enemy(Sprite):

    def on_create(self):
        self.goto_random_position()
        self.scale = 35
        self.color = Color.PURPLE
        self.rotation = random.randint(0, 360)
        self.speed = 4
        self.time = 0
        
        
    def on_update(self, dt):
        self.move_forward(self.speed)

        if self.touching_window_edge():
            self.delete()
        if self.touching_any_sprite_with_tag('bullet'):
            self.delete()

        self.time +=dt

        if self.time > 2:
            b = window.create_sprite(EnemyBullet)
            b.point_toward(player.position)
            b.position = self.position
            
class EnemyBullet(Sprite):

    def on_create(self):
        self.scale = 13
        self.color = Color.ROSE
        self.speed = 6

    def on_update(self, dt):
        self.move_forward(self.speed)
        if self.touching_window_edge():
            self.delete()
        if self.touching_sprite(player):
            self.delete()


def spawn_enemy():
    window.create_sprite(Enemy)


Scheduler.update(spawn_enemy, delay=1)
window.run()