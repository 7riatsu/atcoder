def echo(n, s):
    # nが奇数
    if  n % 2 != 0:
        return "No"
    # nが偶数
    else:
        s_first, s_last = s[:int(n/2)], s[int(n/2):]
        if s_first == s_last:
            return "Yes"
        else:
            return "No"

if __name__ == "__main__":
    n = int(input())
    s = input()
    print(echo(n, s))