def blackjack(A1, A2, A3):
    sum = A1 + A2 + A3
    if sum >= 22:
        return 'bust'
    elif sum <= 21:
        return 'win'


if __name__ == "__main__":
    A1, A2, A3 = map(int, input().split())
    print(blackjack(A1, A2, A3))
