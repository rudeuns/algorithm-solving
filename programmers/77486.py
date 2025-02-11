from collections import defaultdict


def solution(enroll, referral, seller, amount):
    parent = dict(zip(enroll, referral))
    profit = defaultdict(int)

    for s, a in zip(seller, amount):
        money = a * 100
        name = s

        while money > 0 and name != "-":
            p = money // 10
            profit[name] += money - p

            money = p
            name = parent[name]

    answer = [profit[name] for name in enroll]

    return answer
