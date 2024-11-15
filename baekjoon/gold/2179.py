import sys

input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
words = data[1:]

words.sort()

prefixes = set()

for i in range(N - 1):
    sm_len = min(len(words[i]), len(words[i + 1]))

    for j in range(sm_len):
        if words[i + 1].startswith(words[i][: j + 1]):
            prefixes.add(words[i][: j + 1])
        else:
            break

max_len = 0
max_prefix = []

for prefix in prefixes:
    if len(prefix) > max_len:
        max_len = len(prefix)
        max_prefix = [prefix]
    elif len(prefix) == max_len:
        max_prefix.append(prefix)

found = False
prefix_T = ""

for word in data[1:]:
    if not found:
        for prefix in max_prefix:
            if word.startswith(prefix):
                found = True
                prefix_T = prefix
                print(word)
                break
    else:
        if word.startswith(prefix_T):
            print(word)
            break

# sort | set
