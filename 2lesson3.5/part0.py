from pycat.core import Window, Sprite, Color

grid = [
    'pppwpp',
    'pwpwpp',
    'ppwppp',
    'pppppp',
    'pwwwpp',
    'pppppp'
]

color_dict = {'p':"tiles/tile_000.png", 'w':"tiles/tile_001.png"}
print(color_dict['p'])

PIXEL_SIZE = 100
TILE_SIZE = 2
window = Window(width=len(grid[0])*PIXEL_SIZE+200,
                height=len(grid)*PIXEL_SIZE)

class Tile(Sprite):
    current_image = None

    def on_create(self):
        self.scale = TILE_SIZE-0.5
    
    def on_left_click(self):
        Tile.current_image = self.image


class Pixel(Sprite):
    def on_create(self):
        self.scale = PIXEL_SIZE-1
    
    def on_left_click(self):
        if Tile.current_image:
            self.image = Tile.current_image

x0 = PIXEL_SIZE/2
y0 = window.height - PIXEL_SIZE/2

for i in range(len(grid)):
    for j in range(len(grid[i])):
        s = window.create_sprite(Pixel)
        s.x = x0 + j*PIXEL_SIZE
        s.y = y0 - i*PIXEL_SIZE
        s.image = color_dict[grid[i][j]]
        s.width = PIXEL_SIZE-1
        s.height = PIXEL_SIZE-1

tile_list = ["tiles/tile_00"+str(i)+".png" if i < 10 else "tiles/tile_0"+str(i)+".png"
                
                for i in range(100)]
i=0
for y in range(8,window.height,16):
    tile = window.create_sprite(Tile)
    tile.y += y+5
    tile.x = window.width-8
    if i < 100:
        tile.image = tile_list[i]
    i +=1

window.run(is_sharp_pixel_scaling=True)
