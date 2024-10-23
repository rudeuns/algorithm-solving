import sys

read = sys.stdin.read()
data = list(map(int, read.split()))

is_visited = [False for _ in data]
is_made = [False for _ in data]


def dfs(start, cur):
    is_visited[cur] = True
    nxt = data[cur]

    if start == nxt:
        return True
    elif nxt < start or is_visited[nxt] or is_made[nxt]:
        return False

    if dfs(start, nxt):
        is_made[nxt] = True
        is_visited[nxt] = False
        return True
    else:
        is_visited[nxt] = False
        return False


for cur, nxt in enumerate(data[1:], 1):
    if not is_made[cur]:
        is_made[cur] = dfs(cur, cur)

print(is_made.count(True))
for i, check in enumerate(is_made):
    if check:
        print(i)


# dfs
