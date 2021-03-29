N, Y = map(int, input().split())
x, y, z = (-1, -1, -1)

for i in range(N + 1):
    for j in range(N + 1):
        k = N - i - j
        if 10000 * k + 5000 * j + 1000 * i == Y and k >= 0:
            x = k
            y = j
            z = i

print(x, y, z)
