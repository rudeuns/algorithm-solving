import sys
import bisect

lines = sys.stdin.read().strip().split("\n")

n = int(lines[0])
elements = list(map(int, lines[1].split()))

result = [elements[0]]

for num in elements[1:]:
    if result[-1] < num:
        result.append(num)
    else:
        idx = bisect.bisect_left(result, num)
        result[idx] = num

print(len(result))
