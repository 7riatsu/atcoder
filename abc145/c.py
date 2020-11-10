import itertools
import math

def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1/2)

n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))
dist_sum = 0

for team in itertools.permutations(list(range(n)), n):
    for i in range(len(team) - 1):
        dist_sum += distance(arr[team[i]][0], arr[team[i]][1], arr[team[i + 1]][0], arr[team[i + 1]][1])
print(dist_sum / math.factorial(n))