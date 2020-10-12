input_arr = [input() for i in range(3)]
N = input_arr[0]
p_arr = input_arr[1].split(' ')

k = 0
for i in range(len(p_arr)):
    if int(p_arr[i]) == i + 1:
        pass
    else:
        k += 1
if k <= 2:
    print("YES")
else:
    print("NO")