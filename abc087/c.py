n = int(input())

up_arr = list(map(int, input().split()))
down_arr = list(map(int, input().split()))

ans = 0
for i in range(1, n + 1):
    ans = max(ans, sum(up_arr[:i]) + sum(down_arr[i - 1:]))
print(ans)