n, m = map(int, input().split())
arr = [int(i) for i in input().split()]
arr.sort()

diff = []

for i in range(m - 1):
    diff += [arr[i + 1] - arr[i]]
diff.sort(reverse=True)

print(sum(diff[n - 1 :]))
