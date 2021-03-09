A, B, C = map(int, input().split())

ans = False
for i in range(1, B):
    if (A * i) % B == C:
        ans = True
        break

if ans:
    print("YES")
else:
    print("NO")