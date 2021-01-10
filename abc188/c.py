n = int(input())
arr = list(map(int, input().split()))
center_num = len(arr) // 2

l_max, r_max = max(arr[:center_num]), max(arr[center_num:])

print(arr.index(min(l_max, r_max)) + 1)