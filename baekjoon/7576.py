import sys
from collections import deque


def solution(R, C, board):
    t = 0
    queue = deque()  # (r, c, t)

    for r in range(R):
        for c in range(C):
            if board[r][c] == 1:
                queue.append((r, c, t))

    dr, dc = [0, 0, -1, 1], [-1, 1, 0, 0]

    while queue:
        r, c, t = queue.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < R and 0 <= nc < C and board[nr][nc] == 0:
                board[nr][nc] = 1
                queue.append((nr, nc, t + 1))

    for r in range(R):
        for c in range(C):
            if board[r][c] == 0:
                return -1

    return t


if __name__ == "__main__":
    input = sys.stdin.readline
    C, R = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(R)]

    print(solution(R, C, board))
