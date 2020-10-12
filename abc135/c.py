N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

ans = 0
for i in range(N):
    if A[i] < B[i]:
        ans += A[i]
        m = min(A[i+1], B[i] - A[i])
        ans += m
        A[i+1] -= m
    else:
        ans += B[i]
print(ans)