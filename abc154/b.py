def conv(n):
    ans = ''
    for i in range(n):
        ans += 'x'
    return  ans

if __name__ == "__main__":
    s = input()
    print(conv(len(s)))
