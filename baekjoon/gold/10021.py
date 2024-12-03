import sys
import heapq

inputs = sys.stdin.read().splitlines()

N, C = map(int, inputs[0].split())

edges = []

for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        x1, y1 = map(int, inputs[i].split())
        x2, y2 = map(int, inputs[j].split())

        dist = abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2
        if dist >= C:
            heapq.heappush(edges, (dist, i, j))

parent = [i for i in range(N + 1)]


def find_parent(v):
    if v == parent[v]:
        return parent[v]

    parent[v] = find_parent(parent[v])
    return parent[v]


answer = 0
edge_count = 0

while edges:
    dist, v1, v2 = heapq.heappop(edges)

    root1 = find_parent(v1)
    root2 = find_parent(v2)

    if root1 != root2:
        parent[root2] = root1
        answer += dist
        edge_count += 1

    if edge_count == N - 1:
        break

if edge_count < N - 1:
    print(-1)
else:
    print(answer)

# graph
