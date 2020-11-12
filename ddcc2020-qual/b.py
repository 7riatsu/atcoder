n = int(input())
arr = list(map(int, input().split()))

forward = [0] * n
back = [0] * n

for i, ele in enumerate(arr):
    if i == 0:
        forward[i] = ele
    else:
        forward[i] += forward[i - 1] + ele

for i, ele in enumerate(arr[::-1]):
    if i == 0:
        back[i] = sum(arr)
    else:
        back[i] = back[i - 1] - ele

ans = 2020202020
for i in range(len(arr) - 1):
    ans = min(ans, abs(forward[i] - back[i + 1]))
print(ans)