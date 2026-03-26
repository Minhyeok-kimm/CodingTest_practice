def solution(s):
    answer = []
    s_set = set([i for i in s])
    for i in s_set:
        if s.count(i) == 1:
            answer.append(i)
    if not answer:
        return ''
    else:
        answer.sort()
        return ''.join(answer)