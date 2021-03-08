N = int(input())
A = list(map(int, input().split()))

A.sort()

cnt = [0 for _ in range(13)]
for i in range(N):
    cnt[A[i] // 400] += 1
mi = max(1, sum([1 if cnt[i] > 0 else 0 for i in range(8)]))
ma = sum([1 if cnt[i] > 0 else 0 for i in range(8)]) + sum(cnt[8:])
print(mi, ma)