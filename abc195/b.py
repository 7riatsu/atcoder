import math

a, b, w = map(int, input().split())

w *= 1000

l, r = math.ceil(w / b), math.floor(w / a)

if l <= r:
    print(l, r)
else:
    print("UNSATISFIABLE")
