def solution(s):
    answer = 0
    return answer


if __name__ == '__main__':
    # aabbaccc = > expected: 7
    print("> " + solution("aabbaccc"))
    # ababcdcdababcdcd = > expected: 9
    print("> " + solution("ababcdcdababcdcd"))
    # abcabcdede = > expected: 8
    print("> " + solution("abcabcdede"))
    # abcabcabcabcdededededede = > expected: 14
    print("> " + solution("abcabcabcabcdededededede"))
    # xababcdcdababcdcd = > expected: 17
    print("> " + solution("xababcdcdababcdcd"))