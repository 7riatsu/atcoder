n = int(input())
arr = list(map(int, input().split()))

ans = 0

for ele in arr:
    ans += ele - 1
print(ans)