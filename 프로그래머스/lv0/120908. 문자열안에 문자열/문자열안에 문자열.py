def solution(str1, str2):
    target = str1.replace(str2, '!')
    answer = 0
    if '!' in target:
        answer = 1
    else: answer = 2
    return answer