def average_length(s, t, a, b, u):
    if u == s:
        return str(a - 1) + ' ' + str(b)
    elif u == t:
        return str(a) + ' ' + str(b - 1)
    return

if __name__ == "__main__":
    s, t = map(str, input().split())
    a, b = map(int, input().split())
    u = input()
    print(average_length(s, t, a, b, u))