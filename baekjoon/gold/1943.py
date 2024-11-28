import sys

input = sys.stdin.read
data = input().splitlines()

nidx = 0
for _ in range(3):
    N = int(data[nidx])
    coins = []
    total = 0

    for i in range(nidx + 1, nidx + N + 1):
        coin, cnt = map(int, data[i].split())
        coins.append((coin, cnt))
        total += coin * cnt

    nidx += N + 1

    if total % 2 == 1:
        print(0)
        continue

    total = total // 2
    dp = [True] + [False for _ in range(total)]

    result = False
    for coin, cnt in coins:
        for price in range(total - coin, -1, -1):
            if dp[price]:
                for c in range(1, cnt + 1):
                    cur_price = price + coin * c

                    if cur_price > total:
                        break
                    elif cur_price == total:
                        result = True
                        break
                    dp[cur_price] = True
            if result:
                break
        if result:
            break

    if result:
        print(1)
    else:
        print(0)

# dp
