from collections import deque


def solution(board):
    n = len(board)

    dr, dc = [1, 0, -1, 0], [0, 1, 0, -1]
    costs = [[[float("inf")] * 4 for _ in range(n)] for _ in range(n)]

    for r in range(n):
        for c in range(n):
            if board[r][c] == 1 or (r, c) == (0, 0):
                costs[r][c] = [0, 0, 0, 0]

    queue = deque()
    queue.append((0, 0, -1, 0))  # (r, c, direction, cost)

    while queue:
        r, c, d, cost = queue.popleft()

        for nd in range(4):
            nr, nc = r + dr[nd], c + dc[nd]

            if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 0:
                if d == -1 or (d - nd) % 2 == 0:
                    ncost = cost + 100
                else:
                    ncost = cost + 600

                if ncost < costs[nr][nc][nd]:
                    costs[nr][nc][nd] = ncost
                    queue.append((nr, nc, nd, ncost))

    answer = float("inf")

    for i in range(4):
        answer = min(costs[n - 1][n - 1][i], answer)

    return answer
