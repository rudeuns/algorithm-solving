import sys

input = sys.stdin.read
data = input().splitlines()

cases = list(map(int, data[1:]))
cnt = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

for n in cases:
    # 가장 큰 수 계산
    if n % 2 == 0:
        max_num = "1" * (n // 2)
    else:
        max_num = "7" + "1" * (n // 2 - 1)

    # 가장 작은 수 계산
    min_len = (n // 7) + (0 if n % 7 == 0 else 1)
    min_num = ["" for _ in range(min_len)]
    remain = n

    for i in range(min_len):
        st = 1 if i == 0 else 0

        for j in range(st, 10):
            if remain - cnt[j] >= 0 and remain - cnt[j] <= 7 * (min_len - i - 1):
                min_num[i] = str(j)
                remain -= cnt[j]
                break

    print("".join(min_num) + " " + max_num)

# greedy
