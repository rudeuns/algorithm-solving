def solution(cards1, cards2, goal):
    answer = ""

    i1, i2 = 0, 0

    for word in goal:
        if i1 < len(cards1) and cards1[i1] == word:
            i1 += 1
        elif i2 < len(cards2) and cards2[i2] == word:
            i2 += 1
        else:
            answer = "No"
            break
    else:
        answer = "Yes"

    return answer


"""
🎯 Solved (2025.02.10)
"""
