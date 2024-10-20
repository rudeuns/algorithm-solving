import sys

read = sys.stdin.read()
data = read.splitlines()


def is_made(line, ch):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # 가로
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # 세로
        [0, 4, 8], [2, 4, 6]              # 대각선
    ]
    
    return any(all(line[i] == ch for i in condition) for condition in win_conditions)


for line in data[:-1]:
    x_num = line.count('X')
    o_num = line.count('O')
    
    # X는 최대 5개, O는 최대 4개
    if (x_num > 5) or (o_num > 4):
        print('invalid')
        continue

    x_made = is_made(line, 'X')
    o_made = is_made(line, 'O')
    
    if (x_num == o_num and not x_made and o_made) or \
       (x_num - o_num == 1 and x_made and not o_made) or \
       (x_num == 5 and o_num == 4 and not x_made and not o_made):
        print('valid')
    else:
        print('invalid')


# simulation
