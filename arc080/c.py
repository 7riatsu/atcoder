n = int(input())
nums = list(map(int, input().split()))

cnt_arr = [0] * 3

for num in nums:
    if num % 4 == 0:
        cnt_arr[2] += 1
    elif num % 2 == 0:
        cnt_arr[1] += 1
    else:
        cnt_arr[0] += 1

if cnt_arr[0] > cnt_arr[2]:
    if cnt_arr[1] > 0 or cnt_arr[0] > cnt_arr[2] + 1:
        print("No")
        exit()
print("Yes")
