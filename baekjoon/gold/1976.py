import sys

input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
M = int(data[1])
links = [list(map(int, line.split())) for line in data[2:-1]]
travel = list(map(int, data[-1].split()))

parent = [i for i in range(N)]


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(x, y):
    px = find_parent(x)
    py = find_parent(y)

    if px != py:
        parent[py] = px


for i in range(N):
    for j in range(i + 1, N):
        if links[i][j] == 1:
            union(i, j)

answer = "YES"
root = find_parent(travel[0] - 1)

for t in travel[1:]:
    if find_parent(t - 1) != root:
        answer = "NO"
        break

print(answer)

# union-find
