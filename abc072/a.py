N = int(input())
A = list(map(int, input().split()))
A.sort()
arr = [0] * 100000

for num in A:
    arr[num] += 1

ans = 0
for i in range(len(arr) - 2):
    ans = max(ans, arr[i] + arr[i + 1] + arr[i + 2])
print(ans)