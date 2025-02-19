from functools import cmp_to_key


def compare(x, y):
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    else:
        return 0


def solution(numbers):
    nums = list(map(str, numbers))
    nums.sort(key=cmp_to_key(compare))

    answer = str(int("".join(nums)))

    return answer
