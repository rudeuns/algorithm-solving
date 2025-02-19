import heapq


def solution(land, height):
    answer = 0
    n = len(land)

    visited = [[False] * n for _ in range(n)]
    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

    pq = []
    heapq.heappush(pq, (0, 0, 0))  # cost, r, c

    while pq:
        cost, r, c = heapq.heappop(pq)

        if not visited[r][c]:
            visited[r][c] = True
            answer += cost

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]

                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    ncost = abs(land[r][c] - land[nr][nc])

                    if ncost <= height:
                        heapq.heappush(pq, (0, nr, nc))
                    else:
                        heapq.heappush(pq, (ncost, nr, nc))

    return answer
