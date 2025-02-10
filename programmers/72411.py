menu = {}


def select(idx, order, n, result):
    if len(result) == n:
        res = "".join(sorted(result))
        if res not in menu:
            menu[res] = 1
        else:
            menu[res] += 1
        result.pop()
        return

    for i in range(idx, len(order)):
        result.append(order[i])
        select(i + 1, order, n, result)

    if result:
        result.pop()


def solution(orders, course):
    answer = []

    for order in orders:
        n = len(order)

        for c in course:
            if n < c:
                break
            select(0, order, c, [])

    max_cnt = [2] * 11
    max_menu = {}
    for c in course:
        max_menu[c] = []

    for name, cnt in menu.items():
        n = len(name)
        if cnt > max_cnt[n]:
            max_cnt[n] = cnt
            max_menu[n] = [name]
        elif cnt == max_cnt[n]:
            max_menu[n].append(name)

    for value in max_menu.values():
        answer.extend(value)

    answer.sort()

    return answer


"""
🎯 Solved (2025.02.10)
"""
