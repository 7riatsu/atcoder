n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

tp = 0
for ele in sorted(arr):
    p, q = ele[0], ele[1]
    tmp = m - q
    if tmp > 0:
        tp += p * q
        m = tmp
    elif tmp <= 0:
        tp += p * m
        break
print(tp)