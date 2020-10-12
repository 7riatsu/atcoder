input_arr = input().split(" ")
A = int(input_arr[0])
B = int(input_arr[1])

if (A % 2 != B % 2):
    print("IMPOSSIBLE")
else:
    k = int((A + B) / 2)
    print(k)