import sys

inputs = sys.stdin.read().splitlines()
N = int(inputs[0])
origin = list(map(int, inputs[1]))
target = list(map(int, inputs[2]))


def flip(n, cur):
    nxt = []
    for state, count in cur:
        if state[n - 1] == target[n - 1]:
            nxt.append((state, count))
        else:
            state[n - 1] ^= 1
            state[n] ^= 1
            state[n + 1] ^= 1

            nxt.append((state, count + 1))

    return nxt


answer = -1
cases = []

# i = 0
tmp = origin[:]
tmp[0] ^= 1
tmp[1] ^= 1
cases.append((tmp, 1))
cases.append((origin[:], 0))

# i = 1 ~ N - 2
for i in range(1, N - 1):
    cases = flip(i, cases)

# i = N - 1
for state, count in cases:
    if state[N - 2] == target[N - 2] and state[N - 1] == target[N - 1]:
        answer = count if answer < 0 or count < answer else answer
    elif state[N - 2] != target[N - 2] and state[N - 1] != target[N - 1]:
        answer = count + 1 if answer < 0 or count < answer else answer

print(answer)


# greedy
