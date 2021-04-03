from pycat.core import Window, Sprite, Color
from pyglet.image import create
window = Window()

class Cell(Sprite):

    def on_create(self):
        self.height = 70
        self.width = 70
        self.color = Color(0,0,225)

    def create_label(self, value):
        self.value = value
        self.label = window.create_label()
        self.label.text = str(value)
        self.label.x = self.x - self.width/2
        self.label.y = self.y + self.height/2
        self.label.color = Color.BLACK

    def set_color(self, min, max):
        scale = (self.value-min)/(max-min)
        self.color = Color((1-scale)*225, (1-scale)*225, 225)



my_list = [
    [1,2,3,4],
    [-1,2,3,4],
    [-1,-2,3,4],
    [-1,-2,-3,4],
    [-1,-2,-3,-4]
]

list_min = list_max = my_list[0][0]
for i in range(4):
    for j in range(4):
        val = my_list[i][j]
        if val < list_min:
            list_min = val
        if val > list_max:
            list_max = val

print(list_max, list_min)


for i in range(4):
    for j in range(4):
        # print(my_list[i][j], end = " ")
        # print( )
        # label_ij = window.create_label()
        # label_ij.text = str(my_list[i][j])
        # label_ij.x = 400 + j*100
        # label_ij.y = window.height - i*60
        cell = window.create_sprite(Cell)
        cell.x = 500 + j* (cell.width + 1)
        cell.y = 100 + i* (cell.height + 1)
        cell.create_label(my_list[i][j])
        cell.set_color(list_min, list_max)
        

window.run()

