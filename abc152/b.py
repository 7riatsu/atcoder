def compare(a, b):
    a_str = ''
    b_str = ''
    for _ in range(a):
        a_str += str(b)
    for _ in range(b):
        b_str += str(a)

    if int(a_str) > int(b_str):
        return a_str
    else:
        return b_str

if __name__ == "__main__":
    a, b = map(int, input().split(' '))
    print(compare(a, b))