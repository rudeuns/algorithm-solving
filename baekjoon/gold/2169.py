import sys

input = sys.stdin.read
data = input().splitlines()

N, M = map(int, data[0].split())
V = [list(map(int, line.split())) for line in data[1:]]

up = [[0 for _ in range(M)] for _ in range(N)]
left = [[0 for _ in range(M)] for _ in range(N)]
right = [[0 for _ in range(M)] for _ in range(N)]

up[0][0] = left[0][0] = right[0][0] = V[0][0]
for c in range(1, M):
    up[0][c] = left[0][c] = right[0][c] = left[0][c - 1] + V[0][c]

for r in range(1, N):
    for c in range(M):
        up[r][c] = max(up[r - 1][c], max(left[r - 1][c], right[r - 1][c])) + V[r][c]

    left[r][0] = up[r][0]
    for c in range(1, M):
        left[r][c] = max(left[r][c - 1], up[r][c - 1]) + V[r][c]

    right[r][M - 1] = up[r][M - 1]
    for c in range(M - 2, -1, -1):
        right[r][c] = max(right[r][c + 1], up[r][c + 1]) + V[r][c]

print(max(up[N - 1][M - 1], left[N - 1][M - 1]))

# dp
