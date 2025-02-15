from collections import deque


def bfs(n, visited, computers, s):
    queue = deque()
    queue.append(s)
    visited[s] = True

    while queue:
        v1 = queue.popleft()

        for v2 in range(n):
            if computers[v1][v2] == 1 and not visited[v2]:
                queue.append(v2)
                visited[v2] = True


def solution(n, computers):
    answer = 0
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            bfs(n, visited, computers, i)
            answer += 1

    return answer
