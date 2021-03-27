import math
from math import sin, cos

def position(x, y, div):
    angle = 360 / div
    return [x * cos(math.radians(angle)) - y * sin(math.radians(angle)), x * sin(math.radians(angle)) + y * cos(math.radians(angle))]

n = int(input())
x_i, y_i = map(int, input().split())
x_h, y_h = map(int, input().split())

x_c, y_c = (x_h + x_i) / 2, (y_h + y_i) / 2

a, b = position(x_i - x_c, y_i - y_c, n)
print(a + x_c, b + y_c)
