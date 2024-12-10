import sys

input = sys.stdin.readline

N, K, R = map(int, input().split())

road = [[[] for _ in range(N + 1)] for _ in range(N + 1)]
cows = []

for _ in range(R):
    r1, c1, r2, c2 = map(int, input().split())
    road[r1][c1].append((r2, c2))
    road[r2][c2].append((r1, c1))

for _ in range(K):
    r, c = map(int, input().split())
    cows.append((r, c))

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]


def bfs(cr, cc, visited):
    queue = [(cr, cc)]
    visited[cr][cc] = True

    while queue:
        r, c = queue.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if (
                nr <= 0
                or nr > N
                or nc <= 0
                or nc > N
                or visited[nr][nc]
                or ((nr, nc) in road[r][c])
            ):
                continue

            queue.append((nr, nc))
            visited[nr][nc] = True


answer = 0

for i, (cr, cc) in enumerate(cows):
    visited = [[False] * (N + 1) for _ in range(N + 1)]
    bfs(cr, cc, visited)

    for nr, nc in cows[i + 1 :]:
        if not visited[nr][nc]:
            answer += 1

print(answer)

# bfs
