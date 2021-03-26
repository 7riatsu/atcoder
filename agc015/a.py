n, a, b = map(int, input().split())

if n == 1:
    if a == b:
        print(1)
    else:
        print(0)
elif n == 2:
    print(1)
else:
    c = n - 2
    print((b * c - a * c) + 1 if b - a >= 0 else 0)
