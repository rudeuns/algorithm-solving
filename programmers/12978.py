import heapq


def dijkstra(graph, cost, S):
    heap = []
    heapq.heappush(heap, (0, S))
    cost[S] = 0

    while heap:
        c, s = heapq.heappop(heap)

        if c > cost[s]:
            continue

        for e, w in graph[s]:
            if c + w < cost[e]:
                cost[e] = c + w
                heapq.heappush(heap, (cost[e], e))

    return cost


def solution(N, road, K):
    answer = 0

    cost = [float("inf")] * N
    graph = [[] for _ in range(N)]

    for a, b, c in road:
        graph[a - 1].append((b - 1, c))
        graph[b - 1].append((a - 1, c))

    dijkstra(graph, cost, 0)

    for c in cost:
        if c <= K:
            answer += 1

    return answer
