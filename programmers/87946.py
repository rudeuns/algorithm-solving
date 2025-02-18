def solution(k, dungeons):
    answer = 0
    n = len(dungeons)
    visited = [False] * n

    def bt(p, cnt):
        nonlocal answer
        answer = max(answer, cnt)

        for i in range(n):
            if not visited[i] and p >= dungeons[i][0]:
                visited[i] = True
                bt(p - dungeons[i][1], cnt + 1)
                visited[i] = False

    bt(k, 0)

    return answer
