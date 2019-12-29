def execute(N, S, T):
    str = ""
    for i in range(0, N):
        str += S[i] + T[i]
    print(str)

if __name__ == "__main__":
    N = int(input())
    S, T = map(str, input().split())
    execute(N, S, T)