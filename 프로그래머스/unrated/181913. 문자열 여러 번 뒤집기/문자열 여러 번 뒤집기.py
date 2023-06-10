def solution(my_string, queries):
    l = [my_string[i] for i in range(len(my_string))]
    for s, e in queries:
        l[s:e+1] = list(reversed(l[s:e+1]))
    return ''.join(l)
