def solution(n, words):
    answer = [0, 0]

    used = set()
    prev = words[0][0]

    for i, word in enumerate(words):
        if word in used or prev[-1] != word[0]:
            answer = [(i % n) + 1, (i // n) + 1]
            break

        used.add(word)
        prev = word

    return answer
