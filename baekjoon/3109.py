import sys


def solution(R, C, grid):
    answer = 0
    visited = [[False] * C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if grid[r][c] == "x":
                visited[r][c] = True

    for r in range(R):
        stack = [(r, 0)]

        while stack:
            cr, cc = stack.pop()
            visited[cr][cc] = True

            if cc == C - 1:
                answer += 1
                break

            for d in range(1, -2, -1):
                if 0 <= cr + d < R and not visited[cr + d][cc + 1]:
                    stack.append((cr + d, cc + 1))

    return answer


if __name__ == "__main__":
    lines = sys.stdin.read().strip().split("\n")
    R, C = map(int, lines[0].split())

    print(solution(R, C, lines[1:]))
