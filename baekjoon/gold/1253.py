import sys

read = sys.stdin.read()
inputs = list(map(int, read.split()))

N = inputs[0]
data = inputs[1:]
data.sort()

answer = 0

for ti, target in enumerate(data):
    start, end = 0, N - 1

    while start < end:
        sum_val = data[start] + data[end]

        if target < sum_val:
            end -= 1
        elif target > sum_val:
            start += 1
        elif ti == start:
            start += 1
        elif ti == end:
            end -= 1
        else:
            answer += 1
            break

print(answer)

# two-pointer | sort
