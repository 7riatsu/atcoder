n = int(input())
d = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))

d_dict = {}
t_dict = {}

for num in d:
    if num in d_dict:
        d_dict[num] += 1
    else:
        d_dict[num] = 1

for num in t:
    if num in t_dict:
        t_dict[num] += 1
    else:
        t_dict[num] = 1

ans = True
for k, v in t_dict.items():
    if not k in d_dict:
        ans = False
        break

    if v <= d_dict[k]:
        continue
    else:
        ans = False
        break

print("YES" if ans else "NO")
