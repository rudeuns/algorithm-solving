def calc_score(info, result):
    score = 0

    for i, num in enumerate(range(10, -1, -1)):
        if result[i] != 0:
            score += num
        elif info[i] != 0:
            score -= num

    return score


def bt(n, info, win, idx, cur_n, result, answer):
    if cur_n == n or idx == 11:
        result[-1] += n - cur_n

        score = calc_score(info, result)

        if score > answer[0]:
            answer[0] = score
            answer[1] = result[:]
        elif score > 0 and score == answer[0]:
            if result[::-1] > answer[1][::-1]:
                answer[1] = result[:]

        result[-1] -= n - cur_n
        return

    if cur_n + win[idx] <= n:
        result[idx] = win[idx]
        bt(n, info, win, idx + 1, cur_n + win[idx], result, answer)
        result[idx] = 0

    bt(n, info, win, idx + 1, cur_n, result, answer)


def solution(n, info):
    answer = [0, [0] * 11]
    win = [i + 1 for i in info]

    bt(n, info, win, 0, 0, [0] * 11, answer)

    return answer[1] if answer[0] > 0 else [-1]
