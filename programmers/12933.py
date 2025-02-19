def solution(n):
    s = str(n)
    answer = int("".join(sorted(s, reverse=True)))

    return answer
