import math

def solve(x):
    init_money = 100

    i = 0
    while True:
        i += 1
        init_money = math.floor(init_money * 1.01)
        if init_money >= x:
            break
    return i
if __name__ == "__main__":
    x = int(input())
    print(solve(x))