import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
heights = list(map(int, data[1:]))

counts = [0 for _ in range(N)]

for a in range(N):
    max_grad, min_grad = None, None

    for b in range(a + 1, N):
        grad = (heights[b] - heights[a]) / (b - a)

        if max_grad == None or grad > max_grad:
            max_grad = grad
            counts[a] += 1

    for b in range(a - 1, -1, -1):
        grad = (heights[a] - heights[b]) / (a - b)

        if min_grad == None or grad < min_grad:
            min_grad = grad
            counts[a] += 1

answer = 0

for count in counts:
    if answer < count:
        answer = count

print(answer)

# math
