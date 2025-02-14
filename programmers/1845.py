def solution(nums):
    monster = set(nums)

    answer = min(len(nums) // 2, len(monster))

    return answer
