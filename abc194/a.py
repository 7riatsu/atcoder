non_fat, fat = map(int, input().split())

ans = 0

if non_fat + fat >= 15 and fat >= 8:
    ans = 1
elif non_fat + fat >= 10 and fat >= 3:
    ans = 2
elif non_fat + fat >= 3:
    ans = 3
else:
    ans = 4

print(ans)