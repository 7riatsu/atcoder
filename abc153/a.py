def attack(h, a):
    i = 0
    while True:
        i += 1
        h -= a
        if h <= 0:
            break
    return i

if __name__ == "__main__":
    h, a = map(int, input().split())
    print(attack(h, a))