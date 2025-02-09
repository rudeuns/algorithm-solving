import math


def solution(progresses, speeds):
    answer = []
    n = len(progresses)

    days = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(n)]

    fday = days[0]
    num = 0

    for day in days:
        if day <= fday:
            num += 1
        else:
            answer.append(num)
            fday = day
            num = 1
    else:
        answer.append(num)

    return answer


"""
🎯 Solved (2025.02.10)
"""
