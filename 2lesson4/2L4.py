from typing import List
from pycat.core import Window, Sprite, Color

M_ROWS = 6
N_COLS = 10
CELL_SIZE = 100
w = Window(width = N_COLS*CELL_SIZE, height = M_ROWS*CELL_SIZE)

class Cell(Sprite):

    def on_create(self):
        self.scale = CELL_SIZE-1
        self.color = Color.AMBER
    
    def set_ij(self, i, j):
        self.i = i
        self.j = j
        
    def change_color(self):
        if self.color == Color.AMBER:
            self.color = Color.WHITE
        else: self.color = Color.AMBER

    def change_neighbors(self):
        i = self.i
        j = self.j
        if i-1 >= 0:
            grid[i-1][j].change_color()
        if i+1 < M_ROWS:
            grid[i+1][j].change_color()
        if j-1 >= 0:
            grid[i][j-1].change_color()
        if j+1 < N_COLS:
            grid[i][j+1].change_color()

    def on_left_click(self):
        self.change_neighbors()
        self.check_for_win()

    def check_for_win(self):
        for i in range(M_ROWS):
            for j in range(N_COLS):
                if grid[i][j].color == Color.WHITE:
                    return
        print("you win!")

grid: List[List[Cell]] = []
x0 = y0 = CELL_SIZE/2
for i in range(M_ROWS):
    row = []
    for j in range(N_COLS):
        c = w.create_sprite(Cell)
        c.set_ij(i, j)
        c.x = x0 + CELL_SIZE*j
        c.y = y0 + CELL_SIZE*i
        row.append(c)
    grid.append(row)

grid[1][3].change_neighbors()

w.run()