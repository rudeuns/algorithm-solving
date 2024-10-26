import sys
import heapq

read = sys.stdin.read()
inputs = read.splitlines()


def bfs(grid, visited, n):
    queue = []
    heapq.heappush(queue, (grid[0][0], 0, 0))
    visited[0][0] = True

    while queue:
        v, r, c = heapq.heappop(queue)

        if c + 1 < n and not visited[r][c + 1]:
            if r == n - 1 and c + 1 == n - 1:
                return v + grid[r][c + 1]
            heapq.heappush(queue, (v + grid[r][c + 1], r, c + 1))
            visited[r][c + 1] = True

        if c - 1 >= 0 and not visited[r][c - 1]:
            heapq.heappush(queue, (v + grid[r][c - 1], r, c - 1))
            visited[r][c - 1] = True

        if r + 1 < n and not visited[r + 1][c]:
            if r + 1 == n - 1 and c == n - 1:
                return v + grid[r + 1][c]
            heapq.heappush(queue, (v + grid[r + 1][c], r + 1, c))
            visited[r + 1][c] = True

        if r - 1 >= 0 and not visited[r - 1][c]:
            heapq.heappush(queue, (v + grid[r - 1][c], r - 1, c))
            visited[r - 1][c] = True


i, t = 0, 1

while i < len(inputs):
    N = int(inputs[i])
    if N == 0:
        break

    grid, visited = [], []
    for r in range(i + 1, i + N + 1):
        grid.append([v for v in map(int, inputs[r].split())])
        visited.append([False for _ in range(N)])

    print(f"Problem {t}: {bfs(grid, visited, N)}")

    i += N + 1
    t += 1


# graph | dijkstra
