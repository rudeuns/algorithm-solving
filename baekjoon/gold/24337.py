import sys

input = sys.stdin.read
data = input().split()

N, a, b = map(int, data)
answer = []

"""최소 건물 개수의 높이 계산"""
# a - 1개 만큼 1부터 오름차순
for i in range(1, a):
    answer.append(i)

# a, b 공통의 가장 높은 건물
answer.append(a if a > b else b)

# b - 1개 만큼 1까지 내림차순
for i in range(b - 1, 0, -1):
    answer.append(i)

"""N과 사전순 조건에 맞게 1 채우기"""
# 최소 건물 개수보다 N이 작다면 불가능
if len(answer) > N:
    print(-1)
# a가 1이면 이미 가장 높은 건물을 보고 있으므로 그 다음 위치에 1 채우기
elif a == 1:
    print(answer[0], end=" ")

    for _ in range(N - len(answer)):
        print(1, end=" ")

    for ans in answer[1:]:
        print(ans, end=" ")
# a > 1이면 1 높이의 건물이 이미 있으므로 가장 앞쪽에 1 채우기
else:
    for _ in range(N - len(answer)):
        print(1, end=" ")

    for ans in answer:
        print(ans, end=" ")

# greedy
