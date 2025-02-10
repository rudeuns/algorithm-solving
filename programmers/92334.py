def solution(id_list, report, k):
    answer = []

    reported_user, mail_num = {}, {}

    for rep in report:
        user, rp_user = rep.split()

        if rp_user not in reported_user:
            reported_user[rp_user] = set()

        reported_user[rp_user].add(user)

    for value in reported_user.values():
        if len(value) >= k:
            for user in value:
                if user not in mail_num:
                    mail_num[user] = 0

                mail_num[user] += 1

    for user in id_list:
        if user not in mail_num:
            answer.append(0)
        else:
            answer.append(mail_num[user])

    return answer


"""
🎯 Solved (2025.02.10)
"""
