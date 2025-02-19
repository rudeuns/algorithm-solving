def solution(array, commands):
    answer = []

    for i, j, k in commands:
        sliced = array[i - 1 : j]
        sliced.sort()
        answer.append(sliced[k - 1])

    return answer
