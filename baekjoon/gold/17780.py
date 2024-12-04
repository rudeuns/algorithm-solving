import sys

inputs = sys.stdin.read().splitlines()

N, K = map(int, inputs[0].split())

WHITE, RED, BLUE = 0, 1, 2
dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]
dd = [0, 2, 1, 4, 3]

colors = [[BLUE for _ in range(N + 2)] for _ in range(N + 2)]
horses = [[[] for _ in range(N + 2)] for _ in range(N + 2)]

for r, line in enumerate(inputs[1 : N + 1], start=1):
    for c, color in enumerate(map(int, line.split()), start=1):
        colors[r][c] = color

horse_info = []  # [r, c, d]

for idx, line in enumerate(inputs[N + 1 :]):
    r, c, d = map(int, line.split())
    horses[r][c].append(idx)
    horse_info.append([r, c, d])


def move():
    for k in range(K):
        r, c, d = horse_info[k]

        if horses[r][c][0] != k:
            continue

        nr = r + dr[d]
        nc = c + dc[d]

        if colors[nr][nc] == BLUE:
            horse_info[k][2] = dd[d]
            d = dd[d]
            nr = r + dr[d]
            nc = c + dc[d]

        if colors[nr][nc] == WHITE:
            horses[nr][nc] += horses[r][c]
            for hidx in horses[r][c]:
                horse_info[hidx][0] = nr
                horse_info[hidx][1] = nc
            horses[r][c] = []
        elif colors[nr][nc] == RED:
            horses[r][c].reverse()
            horses[nr][nc] += horses[r][c]
            for hidx in horses[r][c]:
                horse_info[hidx][0] = nr
                horse_info[hidx][1] = nc
            horses[r][c] = []


def check_height():
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if len(horses[r][c]) >= 4:
                return True
    return False


answer = -1
for i in range(1, 1001):
    move()
    if check_height():
        answer = i
        break

print(answer)

# simulation
