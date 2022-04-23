def solution(id_list, report, k):
    log_data = {id : set() for id in id_list}
    for log in report:
        user, target = str(log).split(' ')
        log_data[target].add(user)

    answer = {id_: 0 for id_ in id_list}

    for target, ids in log_data.items():
        if len(ids) >= k:
            for id in ids:
                answer[id] += 1

    return list(answer.values())


if __name__ == '__main__':
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
    k = 2

    # exptecd : [2,1,1,0]
    print(solution(id_list, report, k))

    id_list_1 = ["con", "ryan"]
    report_1 = ["ryan con", "ryan con", "ryan con", "ryan con"]
    k_1 = 3

    # exptecd : [0,0]
    print(solution(id_list_1, report_1, k_1))
