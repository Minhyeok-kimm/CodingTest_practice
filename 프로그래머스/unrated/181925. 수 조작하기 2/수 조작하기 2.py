def solution(numLog):
    d = {1:'w', -1:'s', 10:'d', -10:'a'}
    answer = ''
    for i in range(len(numLog)):
        if i != 0:
            answer += d[numLog[i] - numLog[i-1]]
    return answer