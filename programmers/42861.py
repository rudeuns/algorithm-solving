def find_parent(parent, x):
    if x == parent[x]:
        return x

    parent[x] = find_parent(parent, parent[x])
    return parent[x]


def solution(n, costs):
    answer = 0
    edge_num = 0
    parent = [i for i in range(n)]

    costs.sort(key=lambda x: x[2])

    for cost in costs:
        p1 = find_parent(parent, cost[0])
        p2 = find_parent(parent, cost[1])

        if p1 != p2:
            parent[p2] = p1
            answer += cost[2]
            edge_num += 1

            if edge_num == n - 1:
                break

    return answer
