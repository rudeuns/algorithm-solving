def solution(record):
    answer = []
    uid_name = {}

    for rec in record:
        r = rec.split()
        if len(r) == 3:
            uid_name[r[1]] = r[2]

    for rec in record:
        r = rec.split()
        if r[0] == "Enter":
            answer.append(f"{uid_name[r[1]]}님이 들어왔습니다.")
        elif r[0] == "Leave":
            answer.append(f"{uid_name[r[1]]}님이 나갔습니다.")

    return answer


"""
🎯 Solved (2025.02.10)
"""
