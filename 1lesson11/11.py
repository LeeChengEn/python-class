from pycat.core import Window, Sprite, Label

images = [
   'squirrel.jpg',
   'bird.jpg',
   'sheep.jpg',
   'cow.jpg',
   'seal.jpg',
   'cat.jpg',
   'hedgehog.jpg',
   'meerkat.jpg',
]

texts = [
   'Red squirrel',
   'Pheasant',
   'Sheep',
   'Cow',
   'Seal',
   'Cat',
   'Hedgehog',
   'Meerkat',
]

image_number = 0
window = Window(width=1000)
window.background_image = images[image_number]

text_label = Label('', 100, 50)
text_label.text = texts[image_number]
window.add_label(text_label)

likes=[]

class NextButton(Sprite):
   
   def on_left_click(self):
        global image_number
        image_number+=1
        
        if len(images)==image_number:
            window.close()
            return

        window.background_image = images[image_number]
        text_label.text = texts[image_number]

class Tumbsbutton(Sprite):
    def on_left_click(self):

        likes.append(images[image_number])
        print(likes)

       


window.create_sprite(Tumbsbutton,x=700,y=100,scale=0.3,image='thumbs_up.png')
window.create_sprite(NextButton,x=500,y=100,scale=0.5,image='button_next.png')
window.run()