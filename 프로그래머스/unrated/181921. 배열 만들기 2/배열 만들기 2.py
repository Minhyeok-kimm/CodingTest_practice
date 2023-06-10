def solution(l, r):
    answer = []
    lst = ['1', '2', '3', '4', '6', '7', '8', '9']
    for i in range(l, r+1):
        s = True
        for j in range(len(str(i))):
            if str(i)[j] in lst:
                s = False
        if s == True:
            answer.append(i)
    return answer if len(answer) else [-1]