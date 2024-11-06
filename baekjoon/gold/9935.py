import sys

read = sys.stdin.read()
origin, target = read.splitlines()

TN = len(target)
stack = []

for ch in origin:
    stack.append(ch)

    if len(stack) >= TN and "".join(stack[-TN:]) == target:
        del stack[-TN:]

answer = "".join(stack)

if answer:
    print(answer)
else:
    print("FRULA")

# stack
