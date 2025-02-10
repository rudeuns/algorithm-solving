def solution(n, k, cmd):
    answer = ""

    k = k + 1
    up = [i - 1 for i in range(n + 2)]
    down = [i + 1 for i in range(n + 2)]
    rm_stack = []

    for c in cmd:
        if c.startswith("U"):
            _, x = c.split()
            for _ in range(int(x)):
                k = up[k]
        elif c.startswith("D"):
            _, x = c.split()
            for _ in range(int(x)):
                k = down[k]
        elif c == "C":
            rm_stack.append(k)
            down[up[k]] = down[k]
            up[down[k]] = up[k]
            k = up[k] if down[k] > n else down[k]
        elif c == "Z":
            rk = rm_stack.pop()
            down[up[rk]] = rk
            up[down[rk]] = rk

    ans = ["O"] * n

    for rk in rm_stack:
        ans[rk - 1] = "X"

    answer = "".join(ans)

    return answer
