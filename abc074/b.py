n = int(input())
k = int(input())
arr = list(map(int, input().split()))

ans = 0

for ele in arr:
    ans += min(ele, k - ele) * 2
print(ans)