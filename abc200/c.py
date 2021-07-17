import itertools

n = int(input())

arr = [i % 200 for i in list(map(int, input().split()))]

s = set(arr)
ans = 0
for ele in s:
    ans += (arr.count(ele) * (arr.count(ele) - 1)) // 2

print(ans)
