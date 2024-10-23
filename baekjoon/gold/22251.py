import sys

"""숫자 i를 j로 만들기 위해 필요한 반전 led 개수 계산
led_on = [[] for _ in range(10)]
led_on[0] = [1, 1, 1, 1, 1, 1, 0]
led_on[1] = [0, 0, 1, 1, 0, 0, 0]
led_on[2] = [0, 1, 1, 0, 1, 1, 1]
led_on[3] = [0, 1, 1, 1, 1, 0, 1]
led_on[4] = [1, 0, 1, 1, 0, 0, 1]
led_on[5] = [1, 1, 0, 1, 1, 0, 1]
led_on[6] = [1, 1, 0, 1, 1, 1, 1]
led_on[7] = [0, 1, 1, 1, 0, 0, 0]
led_on[8] = [1, 1, 1, 1, 1, 1, 1]
led_on[9] = [1, 1, 1, 1, 1, 0, 1]

reverse_count = [[0 for _ in range(10)] for _ in range(10)]

for i in range(10):
    for j in range(10):
        reverse_count[i][j] = sum(a ^ b for a, b in zip(led_on[i], led_on[j]))

print(reverse_count)
"""

reverse_count = [
    [0, 4, 3, 3, 4, 3, 2, 3, 1, 2],
    [4, 0, 5, 3, 2, 5, 6, 1, 5, 4],
    [3, 5, 0, 2, 5, 4, 3, 4, 2, 3],
    [3, 3, 2, 0, 3, 2, 3, 2, 2, 1],
    [4, 2, 5, 3, 0, 3, 4, 3, 3, 2],
    [3, 5, 4, 2, 3, 0, 1, 4, 2, 1],
    [2, 6, 3, 3, 4, 1, 0, 5, 1, 2],
    [3, 1, 4, 2, 3, 4, 5, 0, 4, 3],
    [1, 5, 2, 2, 3, 2, 1, 4, 0, 1],
    [2, 4, 3, 1, 2, 1, 2, 3, 1, 0],
]

read = sys.stdin.read()
N, K, P, X = map(int, read.split())
answer = 0

for n in range(1, N + 1):
    x = X
    p = 0

    for _ in range(K):
        x, rx = divmod(x, 10)
        n, rn = divmod(n, 10)
        p += reverse_count[rx][rn]

    if p >= 1 and p <= P:
        answer += 1

print(answer)


# simulation
