n = int(input())
arr = list(map(int, input().split()))

print(3 ** len(arr) - 2 ** len([ele for ele in arr if ele % 2 == 0]))
