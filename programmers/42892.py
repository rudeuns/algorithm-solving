import heapq


def make_tree(tree, root, x, idx):
    cur = root

    while True:
        if x < tree[cur]["x"]:
            if "left" in tree[cur]:
                cur = tree[cur]["left"]
            else:
                tree[cur]["left"] = idx
                tree[idx] = {"x": x}
                break
        else:
            if "right" in tree[cur]:
                cur = tree[cur]["right"]
            else:
                tree[cur]["right"] = idx
                tree[idx] = {"x": x}
                break


def search_pre(tree, root):
    result = []
    stack = [root]

    while stack:
        idx = stack.pop()
        result.append(idx)

        if "right" in tree[idx]:
            stack.append(tree[idx]["right"])

        if "left" in tree[idx]:
            stack.append(tree[idx]["left"])

    return result


def search_post(tree, root):
    result = []
    stack = [root]
    visited = [False for _ in range(len(tree) + 1)]

    while stack:
        idx = stack[-1]

        if visited[idx]:
            result.append(stack.pop())
        else:
            visited[idx] = True

            if "right" in tree[idx]:
                stack.append(tree[idx]["right"])

            if "left" in tree[idx]:
                stack.append(tree[idx]["left"])

    return result


def solution(nodeinfo):
    heap = []

    for idx, node in enumerate(nodeinfo, start=1):
        heapq.heappush(heap, (-node[1], node[0], idx))

    tree = {}
    _, x, root = heapq.heappop(heap)
    tree[root] = {"x": x}

    while heap:
        _, x, idx = heapq.heappop(heap)
        make_tree(tree, root, x, idx)

    answer = []

    answer.append(search_pre(tree, root))
    answer.append(search_post(tree, root))

    return answer
