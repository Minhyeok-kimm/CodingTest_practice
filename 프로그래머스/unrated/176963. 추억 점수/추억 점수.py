def solution(name, yearning, photo):
    namedic = dict(zip(name, yearning))
    answer = []
    result = 0
    for i in photo:
        result = 0
        for j in i:
            if j in namedic.keys():
                result += namedic[j]
        answer.append(result)
    return answer