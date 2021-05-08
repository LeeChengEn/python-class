from re import S
from pycat.core import Window, Sprite, Color
from random import choice
from pyglet.image import Texture

WIDTH = 500
HEIGHT = 700
GAP = 10
BUTTON = 5

BUTTON_WIDTH = (WIDTH-(BUTTON+1)*GAP)/BUTTON
BUTTONX = GAP+ BUTTON_WIDTH/2
BUTTONY = GAP+ BUTTON_WIDTH/2

w=Window(WIDTH, HEIGHT)

class ColorChoice(Sprite):
    current_color = None

    def on_create(self):
        self.scale = BUTTON_WIDTH
        self.y = BUTTONY
        self.x = BUTTONX
        
    def on_left_click (self):
        ColorChoice.current_color = self.color


class ColorCode(Sprite):

    def on_create(self):
        self.scale = 0.75*BUTTON_WIDTH
        self.y = HEIGHT-BUTTONY
        self.x = BUTTONX


class ColorGuess(Sprite):

    def on_create(self):
        self.scale = 0.75*BUTTON_WIDTH
        self.y = BUTTONY
        self.x = BUTTONX
        
    def on_left_click (self):
        if ColorChoice.current_color:
            self.color = ColorChoice.current_color


class CheckButton(Sprite):

    def on_create(self):
        self.scale = 0.66*BUTTON_WIDTH
        self.y = BUTTONY
        self.x = WIDTH - BUTTONX
        self.color = Color.WHITE
        self.current_guess = 0
        self.red_score = 0
        self.white_score = 0

    def get_score(self):
        self.red_score = 0
        for i in range(len(code_list)):
            if guess_list[i].color == code_list[i].color:
                self.red_score += 1
        print(self.red_score)

    def on_left_click(self):
        self.get_score()
        draw_red_pegs(self.red_score, self.current_guess)
        if is_match():
            win()
        else:
            self.current_guess +=1
            if self.current_guess >5:
                lose()
            else:
                make_new_guess(self.current_guess)
        
check = w.create_sprite(CheckButton)

def draw_red_pegs(red_pegs, guess):
    for i in range(red_pegs):
        s = w.create_sprite()
        s.scale = 10
        s.color = Color.RED
        s.y = BUTTONY
        s.y += guess*75 + BUTTONY+50
        s.x = w.width - 20 - (i*20)

def is_match():
    for i in range(len(code_list)):
        if guess_list[i].color != code_list[i].color:
            return False
    return True

def win():
    print("you win")

def lose():
    print("you lose")

def  make_new_guess(guess):
    guess_list.clear()
    for i in range(BUTTON-1):
        s = w.create_sprite(ColorGuess)
        s.x += i*(BUTTON_WIDTH+GAP)
        s.y += guess*75 + BUTTONY+50
        guess_list.append(s)


color_list = [Color.RED, Color.GREEN, Color.BLUE, Color.PURPLE]
for i in range(BUTTON-1):
    color = w.create_sprite(ColorChoice)
    color.x += i*(BUTTON_WIDTH+GAP)
    color.color = color_list[i]

code_list = []
color_list = [Color.RED, Color.GREEN, Color.BLUE, Color.PURPLE]
for i in range(BUTTON-1):
    s = w.create_sprite(ColorCode)
    s.x += i*(BUTTON_WIDTH+GAP)
    s.color = choice(color_list)
    code_list.append(s)

guess_list = []
for i in range(BUTTON-1):
    s = w.create_sprite(ColorGuess)
    s.x += i*(BUTTON_WIDTH+GAP)
    s.y += BUTTONY+50
    guess_list.append(s)


w.run()