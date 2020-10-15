x = int(input())

a = x // 100
b = x % 100

if 0 <= b <= a * 5:
    print(1)
else:
    print(0)
