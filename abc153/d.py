j = 0

def attack(x):
    global j
    if x == 1:
        j += 1
        return
    elif x % 2 == 1:
        x = x // 2
        j += 1
    else:
        x = int(x / 2)
        j += 1
    attack(x)

if __name__ == "__main__":
    h = int(input())
    attack(h)
    print(2 ** j - 1)