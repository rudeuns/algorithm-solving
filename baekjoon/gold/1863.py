import sys

inputs = sys.stdin.read().splitlines()

stack = [0]
answer = -1

for data in inputs[1:]:
    _, y = map(int, data.split())

    while len(stack) > 0:
        if stack[-1] < y:
            stack.append(y)
            break
        elif stack[-1] > y:
            stack.pop()
            answer += 1
        else:
            break

answer += len(stack)

print(answer)


# stack
