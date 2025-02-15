def dfs(n, edges, v1, v2):
    visited = [False] * (n + 1)
    stack = []

    stack.append(v1)
    visited[v1] = True
    cnt = 1

    while stack:
        s = stack.pop()

        for e in edges[s]:
            if (s, e) == (v1, v2) or (s, e) == (v2, v1):
                continue

            if not visited[e]:
                stack.append(e)
                visited[e] = True
                cnt += 1

    return abs(cnt - (n - cnt))


def solution(n, wires):
    answer = n

    edges = [[] for _ in range(n + 1)]

    for v1, v2 in wires:
        edges[v1].append(v2)
        edges[v2].append(v1)

    for v1, v2 in wires:
        diff = dfs(n, edges, v1, v2)
        answer = min(diff, answer)

    return answer
