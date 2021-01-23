import string

n = int(input())
s = input()

ans = 0

for i in range(1, n):
    cnt = 0
    for char in string.ascii_lowercase:
        left, right = False, False

        for j in range(0, i):
            if s[j] == char:
                left = True

        for k in range(i, n):
            if s[k] == char:
                right = True
        if left == True and right == True:
            cnt += 1
        if cnt >= ans:
            ans = cnt
print(ans)