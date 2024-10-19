import sys
import heapq

read = sys.stdin.read()
data = read.splitlines()

N, _ = map(int, data[0].split())

# link[출발 노드] = [(도착 노드, 비용), ...]
link = [[] for _ in range(N + 1)]
for line in data[1:]:
    v1, v2, w = map(int, line.split())
    link[v1].append((v2, w))
    link[v2].append((v1, w))

# 1번 노드로부터 들어가는 최소 비용
min_w = [-1 for _ in range(N + 1)]
min_w[1] = 0

# queue = [(현재 비용, 현재 노드), ...]
# min heap으로 갱신 횟수 최소화
queue = [(0, 1)]
while queue:
    cur_w, cur_v = heapq.heappop(queue)

    if cur_w > min_w[cur_v]:
        continue

    for nxt_v, nxt_w in link[cur_v]:
        if min_w[nxt_v] < 0 or min_w[cur_v] + nxt_w < min_w[nxt_v]:
            min_w[nxt_v] = min_w[cur_v] + nxt_w
            heapq.heappush(queue, (min_w[nxt_v], nxt_v))

print(min_w[N])

# graph | dijkstra
