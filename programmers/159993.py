from collections import deque


def dfs(sr, sc, target, maps):
    R, C = len(maps), len(maps[0])
    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

    visited = [
        [True if maps[r][c] == "X" else False for c in range(C)] for r in range(R)
    ]

    queue = deque()
    queue.append((sr, sc, 0))
    visited[sr][sc] = True

    while queue:
        r, c, t = queue.popleft()

        if maps[r][c] == target:
            return t

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                queue.append((nr, nc, t + 1))
                visited[nr][nc] = True

    return -1


def solution(maps):
    R, C = len(maps), len(maps[0])
    sr, sc = 0, 0
    lr, lc = 0, 0

    for r in range(R):
        for c in range(C):
            if maps[r][c] == "S":
                sr, sc = r, c
            elif maps[r][c] == "L":
                lr, lc = r, c

    result1 = dfs(sr, sc, "L", maps)
    if result1 == -1:
        return -1

    result2 = dfs(lr, lc, "E", maps)
    if result2 == -1:
        return -1

    return result1 + result2
