def bt(n, r, col, diagR, diagL):
    answer = 0

    if r == n:
        answer += 1
        return answer

    for c in range(n):
        if not col[c] and not diagR[r + c] and not diagL[r - c + n]:
            col[c] = diagR[r + c] = diagL[r - c + n] = True

            answer += bt(n, r + 1, col, diagR, diagL)

            col[c] = diagR[r + c] = diagL[r - c + n] = False

    return answer


def solution(n):
    col = [False] * n
    diagR, diagL = [False] * (n * 2), [False] * (n * 2)

    answer = bt(n, 0, col, diagR, diagL)

    return answer
