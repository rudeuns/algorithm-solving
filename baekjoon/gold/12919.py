import sys

read = sys.stdin.read()
S, T = read.split()


# T에서 제거하는 방식의 역추적 알고리즘
def backtracking(cur_T):
    if len(cur_T) == len(S):
        if cur_T == S:
            return True
        return False

    # T가 A로 끝나는 경우 단순 제거
    if cur_T[-1] == "A" and backtracking(cur_T[:-1]):
        return True

    # T가 B로 시작하는 경우 뒤집고 제거
    if cur_T[0] == "B" and backtracking(cur_T[::-1][:-1]):
        return True

    return False


if backtracking(T):
    print(1)
else:
    print(0)


# backtracking
