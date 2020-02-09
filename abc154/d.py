n, k = map(int, input().split())
arr = list(map(int,input().split()))
sum_tmp = [sum(arr[i:i+k]) for i in range(n - (k - 1))]
max_v = max(sum_tmp)
max_i = sum_tmp.index(max_v)
ans = 0
for j in arr[max_i:max_i+k]:
    ans += sum(range(1, j+1)) / j
print(ans)