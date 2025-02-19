def solution(s):
    answer = []

    s = s[2:-2].split("},{")

    arr = []
    for el in s:
        arr.append(list(map(int, el.split(","))))

    arr.sort(key=len)

    for nums in arr:
        for num in nums:
            if num not in answer:
                answer.append(num)

    return answer
