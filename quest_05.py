def solution(record):
    answer = []
    logs = []
    users = {}
    for log in record:
        data = log.split(' ')
        user_log = {
            'id': data[1],
            'status': data[0]
        }
        if user_log['status'] == 'Enter':
            users[user_log['id']] = data[2]
            logs.append(user_log)
        elif user_log['status'] == 'Leave':
            logs.append(user_log)
        elif user_log['status'] == 'Change':
            users[user_log['id']] = data[2]

    for log in logs:
        text = users[log['id']] + '님이'
        if log['status'] == 'Enter':
            text += ' 들어왔습니다.'
        elif log['status'] == 'Leave':
            text += ' 나갔습니다.'

        answer.append(text)

    return answer


if __name__ == '__main__':
    # record : ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
    # result : ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
    print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
