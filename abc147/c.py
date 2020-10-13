N = int(input())
statement = {}
ans = 0
for i in range(N):
    l = []
    n = int(input())
    for j in range(n):
        l.append(list(map(int, input().split())))
    statement[i+1] = l

def det(stat, hypo):
    D = True
    for i in range(1, N+1):
        if hypo[i] == "1":
            for j in range(len(stat[i])):
                if int(hypo[stat[i][j][0]]) != stat[i][j][1]:
                    D = False
                    break
        if D == False:
            break
    return D

for i in range(2**N):
    Hypo = format(2**N - i - 1, "017b")[-(N+1):]
    if Hypo.count("1") > ans:
        if det(statement, Hypo):
            ans = Hypo.count("1")
print(ans)
# print(N, statement, l, n)