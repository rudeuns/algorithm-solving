def solution(s):
    answer = [0, 0]  # [변환 횟수, 제거된 0의 개수]

    while s != "1":
        ns = ""

        for c in s:
            if c == "0":
                answer[1] += 1
            else:
                ns += "1"

        ns = len(ns)
        s = ""

        while ns > 0:
            s = str(ns % 2) + s
            ns = ns // 2

        answer[0] += 1

    return answer
