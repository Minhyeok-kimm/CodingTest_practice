def solution(babbling):
    possible = ['aya', 'ye', 'woo', 'ma']
    answer = 0
    for i in range(len(babbling)):
        for j in possible:
            babbling[i] = babbling[i].replace(j, ' ')
        if len(babbling[i].replace(' ', '')) == 0:
            answer += 1
    return answer