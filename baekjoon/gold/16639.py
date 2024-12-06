import sys

inputs = sys.stdin.read().splitlines()

N = (int(inputs[0]) + 1) // 2

max_dp = [[-sys.maxsize for _ in range(N)] for _ in range(N)]
min_dp = [[sys.maxsize for _ in range(N)] for _ in range(N)]
op = ["" for _ in range(N)]

idx = 0
for i, ch in enumerate(inputs[1]):
    if i % 2 == 0:
        max_dp[idx][idx] = min_dp[idx][idx] = int(ch)
        idx += 1
    else:
        op[idx] = ch


def operation(ch, a, b):
    if ch == "*":
        return a * b
    elif ch == "+":
        return a + b
    elif ch == "-":
        return a - b


def max_compare(a, b, c, d):
    e = a if a > b else b
    f = c if c > d else d
    return e if e > f else f


def min_compare(a, b, c, d):
    e = a if a < b else b
    f = c if c < d else d
    return e if e < f else f


for step in range(1, N):
    for start in range(N - 1):
        end = start + step
        if end >= N:
            break

        for mid in range(start, end):
            a = operation(op[mid + 1], max_dp[start][mid], max_dp[mid + 1][end])
            b = operation(op[mid + 1], max_dp[start][mid], min_dp[mid + 1][end])
            c = operation(op[mid + 1], min_dp[start][mid], min_dp[mid + 1][end])
            d = operation(op[mid + 1], min_dp[start][mid], max_dp[mid + 1][end])

            max_val = max_compare(a, b, c, d)
            min_val = min_compare(a, b, c, d)

            max_dp[start][end] = (
                max_val if max_val > max_dp[start][end] else max_dp[start][end]
            )
            min_dp[start][end] = (
                min_val if min_val < min_dp[start][end] else min_dp[start][end]
            )

print(max_dp[0][N - 1])

# dp
