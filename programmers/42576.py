def solution(participant, completion):
    answer = ""
    dic = {}

    for comp in completion:
        if comp not in dic:
            dic[comp] = 1
        else:
            dic[comp] += 1

    for part in participant:
        if part not in dic or dic[part] == 0:
            answer = part
            break
        else:
            dic[part] -= 1

    return answer


"""
🎯 Solved (2025.02.10)
"""
