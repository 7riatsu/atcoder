def check(s):
    if kaibun(s) and kaibun(s[0:int((len(s) - 1) / 2)]) and kaibun(s[int((len(s) + 3) / 2) - 1:len(s)]):
        return 'Yes'
    else:
        return 'No'

def kaibun(s):
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return False
    return True

if __name__ == "__main__":
    s = input()
    print(check(s))