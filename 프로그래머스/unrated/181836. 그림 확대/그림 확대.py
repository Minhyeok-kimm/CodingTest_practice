def solution(picture, k):
    answer = []
    arr = []
    for i in picture:
        s = ''
        for j in range(len(i)):
            s += i[j]*k
        answer.append(s)
    for a in answer:
        for b in range(k):
            arr.append(a)
    return arr