from collections import deque


def solution(maps):
    answer = -1

    R, C = len(maps), len(maps[0])
    visited = [[not maps[r][c] for c in range(C)] for r in range(R)]

    queue = deque()
    queue.append((0, 0, 1))
    visited[0][0] = True

    dr, dc = [0, 0, -1, 1], [-1, 1, 0, 0]

    while queue:
        r, c, cnt = queue.popleft()

        if r == R - 1 and c == C - 1:
            answer = cnt
            break

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                queue.append((nr, nc, cnt + 1))
                visited[nr][nc] = True

    return answer
