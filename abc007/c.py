from collections import deque

r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
maze = [list(input()) for _ in range(r)]
vs = [[float('inf')] * c for _ in range(r)]

q = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
    vs[sy - 1][sx - 1] = 0
    q.append([sy, sx])
    while len(q) > 0:
        p = q.popleft()
        if p[0] == gy and p[1] == gx:
            break
        for i in range(len(dx)):
            y = p[0] + dy[i]
            x = p[1] + dx[i]
            if 0 <= x - 1 < c and 0 <= y - 1 < r and maze[y - 1][x - 1] != '#' and vs[y - 1][x - 1] == float('inf'):
                q.append([y, x])
                vs[y - 1][x - 1] = vs[p[0] - 1][p[1] - 1] + 1
    return vs[gy - 1][gx - 1]

print(bfs())
