from collections import deque

d = deque()

n = int(input())
a = map(int, input().split())

for i, ele in enumerate(a):
    if i % 2 == 0:
        d.appendleft(ele)
    else:
        d.append(ele)

if i % 2 != 0:
    d.reverse()

print(*d)
