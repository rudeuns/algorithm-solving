from collections import deque, defaultdict


def solution(info, edges):
    answer = 0

    child = defaultdict(list)

    for edge in edges:
        child[edge[0]].append(edge[1])

    queue = deque()
    queue.append(([0], 1, 0))  # path, sheep, wolf

    while queue:
        path, sheep, wolf = queue.popleft()
        answer = max(answer, sheep)

        for pid in path:
            for cid in child[pid]:
                if cid not in path:
                    if info[cid] == 0:
                        queue.append((path[:] + [cid], sheep + 1, wolf))
                    elif wolf + 1 < sheep:
                        queue.append((path[:] + [cid], sheep, wolf + 1))

    return answer
