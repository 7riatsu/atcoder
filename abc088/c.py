from itertools import permutations
matrix = [list(map(int, input().split())) for _ in range(3)]

if not matrix[0][0] - matrix[1][0] == matrix[0][1] - matrix[1][1] == matrix[0][2] - matrix[1][2]:
    print("No")
    exit()
if not matrix[1][0] - matrix[2][0] == matrix[1][1] - matrix[2][1] == matrix[1][2] - matrix[2][2]:
    print("No")
    exit()
if not matrix[2][0] - matrix[0][0] == matrix[2][1] - matrix[0][1] == matrix[2][2] - matrix[0][2]:
    print("No")
    exit()

print("Yes")
