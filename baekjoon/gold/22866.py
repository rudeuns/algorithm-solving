import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
heights = [0] + list(map(int, data[1:]))  # 인덱스 1부터 시작

# (보이는 건물 개수, 가장 가까운 건물 위치)
left = [(0, 0) for _ in range(N + 1)]
right = [(0, 0) for _ in range(N + 1)]

# 왼쪽 방향 보이는 건물 계산
for cur in range(2, N + 1):
    nxt = cur - 1
    while nxt > 0:
        if heights[cur] < heights[nxt]:
            left[cur] = (left[nxt][0] + 1, nxt)
            break
        elif heights[cur] == heights[nxt]:
            left[cur] = left[nxt]
            break
        else:
            nxt = left[nxt][1]

# 오른쪽 방향 보이는 건물 계산
for cur in range(N - 1, 0, -1):
    nxt = cur + 1
    while nxt > 0:
        if heights[cur] < heights[nxt]:
            right[cur] = (right[nxt][0] + 1, nxt)
            break
        elif heights[cur] == heights[nxt]:
            right[cur] = right[nxt]
            break
        else:
            nxt = right[nxt][1]

for i in range(1, N + 1):
    total = left[i][0] + right[i][0]

    if total == 0:
        print(0)
    elif left[i][1] == 0 or right[i][1] == 0:
        print(f"{total} {max(left[i][1], right[i][1])}")
    else:
        left_dist = i - left[i][1]
        right_dist = right[i][1] - i
        pos = left[i][1] if left_dist <= right_dist else right[i][1]
        print(f"{total} {pos}")
