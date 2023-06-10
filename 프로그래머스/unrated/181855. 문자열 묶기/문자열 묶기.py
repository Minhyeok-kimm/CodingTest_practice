def solution(strArr):
    strlen = [len(i) for i in strArr]
    answer = []
    for i in range(1, max(strlen)+1):
        answer.append(strlen.count(i))
    return max(answer)