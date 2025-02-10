from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []

    for c in course:
        menu = []

        for order in orders:
            menu += combinations(sorted(order), c)

        counter = Counter(menu)
        sorted_counter = counter.most_common()

        max_cnt = 2
        for menu_tuple, cnt in sorted_counter:
            if cnt < max_cnt:
                break
            else:
                max_cnt = cnt
                answer.append("".join(menu_tuple))

    answer.sort()

    return answer
