import math

a, b, c, d = map(int, input().split())

lcm = c * d // math.gcd(c, d)
x = b - b // c - b // d + b // lcm
y = (a - 1) - (a - 1) // c - (a - 1) // d + (a - 1) // lcm
print(x - y)
