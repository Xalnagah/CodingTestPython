def solution(s):
    answer = len(s)
    for i in range(len(s)//2):
        cmp_str = cmp_2(s, i+1)
        answer = min(answer, len(cmp_str))
    return answer


def cmp(s, num):
        c = 0
        tmp_str = ''
        cmp_str = ''
        while len(s) > 0:
            if len(s) < num:
                num = len(s)

            txt = s[:num]
            s = s[num:]
            if tmp_str == txt:
                c += 1
            elif c > 0:
                if c > 1:
                    cmp_str += str(c)
                cmp_str += tmp_str
                tmp_str = txt
                c = 1
            else:
                tmp_str = txt
                c = 1
            # 마지막 값
            if len(s) == 0:
                if c > 1:
                    cmp_str += str(c)
                cmp_str += tmp_str

        return cmp_str


def cmp_2(s, num):
    str_list = [s[i:i+num] for i in range(0, len(s), num)]
    cmp_str = ''
    cnt = 1
    for txt1, txt2 in zip(str_list, str_list[1:]+['']):
        if txt1 == txt2:
            cnt += 1
        else:
            if cnt > 1:
                cmp_str += str(cnt)
            cmp_str += txt1
            cnt = 1
    return cmp_str


if __name__ == '__main__':
    # aabbaccc = > expected: 7
    print('aabbaccc > ', solution('aabbaccc'))
    # ababcdcdababcdcd = > expected: 9
    print('ababcdcdababcdcd > ', solution('ababcdcdababcdcd'))
    # abcabcdede = > expected: 8
    print('abcabcdede > ', solution("abcabcdede"))
    # abcabcabcabcdededededede = > expected: 14
    print('abcabcabcabcdededededede > ', solution('abcabcabcabcdededededede'))
    # xababcdcdababcdcd = > expected: 17
    print('xababcdcdababcdcd > ', solution('xababcdcdababcdcd'))
