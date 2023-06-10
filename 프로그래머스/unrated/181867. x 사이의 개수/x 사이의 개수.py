def solution(myString):
    answer = []
    lst = myString.split('x')
    for i in range(len(lst)):
        answer.append(len(lst[i]))
    return answer