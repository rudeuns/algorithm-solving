import sys


def count_ch(w, k):
    # 각 알파벳 문자가 나타난 위치를 저장
    pos_ch = {}

    for i, ch in enumerate(w):
        if not pos_ch.get(ch):
            pos_ch[ch] = [i]
        else:
            pos_ch[ch].append(i)

    # 각 알파벳 문자를 k개 포함하는 문자열 길이 계산
    min_len = -1
    max_len = -1

    for pos_li in pos_ch.values():
        if len(pos_li) < k:
            continue

        for i in range(k - 1, len(pos_li)):
            cur_len = pos_li[i] - pos_li[i - k + 1] + 1

            if min_len < 0 or cur_len < min_len:
                min_len = cur_len

            if cur_len > max_len:
                max_len = cur_len

    if min_len < 0:
        print(-1)
    else:
        print(f"{min_len} {max_len}")


read = sys.stdin.read()
data = read.split()

for i in range(1, len(data), 2):
    count_ch(data[i], int(data[i + 1]))


# String | Sliding Window
