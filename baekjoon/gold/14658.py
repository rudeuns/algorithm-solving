import sys

input = sys.stdin.read
data = input().splitlines()

X, Y, L, K = map(int, data[0].split())
pos = [tuple(map(int, d.split())) for d in data[1:]]
pos.sort()

max_out = 1

# 1. 트램펄린 왼쪽 모서리 기준 설정
for i in range(K):
    min_x, max_x = pos[i][0], pos[i][0] + L
    bottom_min_y, bottom_max_y = pos[i][1] - L, pos[i][1]  # pos[i]는 포함되도록 설정

    # 2. 트램펄린 아래쪽 모서리 기준 설정
    for j in range(i + 1, K):
        if pos[j][0] > max_x:
            break
        elif pos[j][1] < bottom_min_y or pos[j][1] > bottom_max_y:
            continue

        min_y, max_y = pos[j][1], pos[j][1] + L

        # 3. 위치가 정해진 트램펄린에 포함된 별똥별 수 계산
        out = 1
        for k in range(i + 1, K):
            if pos[k][0] > max_x:
                break
            elif pos[k][1] < min_y or pos[k][1] > max_y:
                continue

            out += 1

        max_out = out if out > max_out else max_out

print(K - max_out)
