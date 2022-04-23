def solution(lottos, win_nums):
    rank_book = {
        6 : 1,
        5 : 2,
        4 : 3,
        3 : 4,
        2 : 5,
        1 : 6,
        0 : 6,
    }
    win_cnt = 0
    max_cnt = 0
    for l in lottos:
        if l == 0:
            max_cnt += 1
            continue
        for w in win_nums:
            if l == w:
                win_cnt += 1
    max_cnt += win_cnt
    answer = [rank_book.get(max_cnt), rank_book.get(win_cnt)]
    return answer


if __name__ == '__main__':
    lottos = [44, 1, 0, 0, 31, 25]
    win_nums = [31, 10, 45, 1, 6, 19]
    # exptected : [3, 5]
    print(solution(lottos, win_nums))

    lottos_1 = [0, 0, 0, 0, 0, 0]
    win_nums_1 = [38, 19, 20, 40, 15, 25]
    # exptected : [1, 6]
    print(solution(lottos_1, win_nums_1))

    lottos_2 = [45, 4, 35, 20, 3, 9]
    win_nums_2 = [20, 9, 3, 45, 4, 35]
    # exptected : [1, 1]
    print(solution(lottos_2, win_nums_2))