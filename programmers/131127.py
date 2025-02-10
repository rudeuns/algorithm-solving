def solution(want, number, discount):
    answer = 0

    dic_want = {}
    for i, w in enumerate(want):
        dic_want[w] = number[i]

    for i in range(len(discount) - 9):
        dic_item = {}

        for item in discount[i : i + 10]:
            if item in dic_item:
                dic_item[item] += 1
            else:
                dic_item[item] = 1

        if dic_want == dic_item:
            answer += 1

    return answer


"""
🎯 Solved (2025.02.10)
"""
