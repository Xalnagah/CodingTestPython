import re


def solution(new_id):
    # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    answer = new_id.lower()
    # print('1. 단계 : ', answer)

    # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    answer = re.sub(r'[^a-z0-9-_.]', '', answer)
    # print('2. 단계 : ', answer)

    # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    answer = re.sub(r'[.]{2,}', '.', answer)
    # print('3. 단계 : ', answer)

    # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    answer = re.sub(r'^[.]|[.]$', '', answer)
    # print('4. 단계 : ', answer)

    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    # answer = len(answer) == 0 if 'a' else answer
    if len(answer) == 0:
        answer = 'a'
    # print('5. 단계 : ', answer)

    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    # 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    if len(answer) >= 16:
        answer = answer[:15]
        answer = re.sub(r'[.]$', '', answer)
    # print('6. 단계 : ',  answer)

    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    if len(answer) <= 2:
        w = answer[-1]
        for i in range(3-len(answer)):
                answer += w
    # print('7. 단계 : ', answer);

    return answer


if __name__ == '__main__':
    # case 1. expected "bat.y.abcdefghi"
    result1 = solution('...!@BaT#*..y.abcdefghijklm')
    print('expected : "bat.y.abcdefghi" ->', 'answer :', result1, '->', 'bat.y.abcdefghi' == result1)

    # case 2. expected "z--"
    result2 = solution('z-+.^.')
    print('expected : "z--" ->', 'answer :', result2, '->', 'z--' == result2)
    # print("expected : z-- -> answer : " + solution("z-+.^."))

    # case 3. expected "aaa"
    result3 = solution('=.=')
    print("expected : aaa -> answer : " + result3, '->', 'aaa' == result3)

    # case 4. expected "123_.def"
    result4 = solution("123_.def")
    print("expected : 123_.def -> answer : " + result4, '->', '123_.def' == result4)

    # case 5. expected "abcdefghijklmn"
    result5 = solution("abcdefghijklmn.p")
    print("expected : abcdefghijklmn -> answer : " + result5, '->', 'abcdefghijklmn' == result5)
