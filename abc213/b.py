n = int(input())
arr = list(map(int, input().split()))
print(arr.index(sorted(arr)[-2]) + 1)