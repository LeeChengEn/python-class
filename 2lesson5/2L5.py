from pycat.core import Window, Point
from math import sqrt

w = Window()

point_a = Point(500,200)
point_b = Point(300,200)
c = abs(point_b.x - point_a.x)
a = c/2 
b = sqrt(c**2-a**2)
point_c = (point_a + point_b)/2
point_c.y += b
line_ab = w.create_line(point_a.x, point_a.y, point_b.x, point_b.y)
line_ac = w.create_line(point_a.x, point_a.y, point_c.x, point_c.y)
line_bc = w.create_line(point_c.x, point_c.y, point_b.x, point_b.y)

w.run()