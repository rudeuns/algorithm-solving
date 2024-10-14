import sys

N = 10000

# use 1
count = [1 for _ in range(N + 1)]

# use 2
for i in range(2, N + 1):
    count[i] += count[i - 2]

# use 3
for i in range(3, N + 1):
    count[i] += count[i - 3]


read = sys.stdin.read()
data = read.split()

nums = map(int, data[1:])

for n in nums:
    print(count[n])


# DP
