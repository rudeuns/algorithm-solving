import sys

read = sys.stdin.read()
inputs = read.split()
N, C = int(inputs[0]), int(inputs[1])
pos = list(map(int, inputs[2:]))
pos.sort()

# 가능한 최소 거리, 최대 거리
start = 1
end = pos[-1] - pos[0]

answer = 1

while start <= end:
    mid = (start + end) // 2

    # mid 거리로 공유기 C개 이상 설치 가능한 지 확인
    # 가능하면 mid를 늘리고, 불가능하면 mid를 줄이기

    # 1번 집에 설치하고 시작
    cnt = 1
    cur = pos[0]

    for i in range(1, N):
        if pos[i] >= cur + mid:
            cnt += 1
            cur = pos[i]

    if cnt >= C:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)

# binary search
