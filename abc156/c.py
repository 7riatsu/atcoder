n = int(input())
arr = list(map(int, input().split()))

ans = 100000000000000
for i in range(min(arr), max(arr) + 1):
    tmp = sum([(ele - i) ** 2 for ele in arr])
    ans = min(ans, tmp)
print(ans)