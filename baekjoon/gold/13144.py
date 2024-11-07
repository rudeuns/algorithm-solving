import sys

input = sys.stdin.read
data = input().split()

nums = list(map(int, data[1:]))
last_pos = [-1 for _ in range(100001)]
start, end = 0, 0  # 큐의 시작과 끝 인덱스
answer = 0

for pos, num in enumerate(nums):
    # 현재 추가되는 숫자가 이미 큐에 있다면 그 숫자까지 큐에서 제거
    if last_pos[num] >= start:
        start = last_pos[num] + 1

    last_pos[num] = pos
    end += 1  # 큐에 추가
    answer += end - start

print(answer)

# two pointer
