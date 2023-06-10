def solution(n, control):
    s = {'w':1, 's':-1, 'd':10, 'a':-10}
    for i in control:
        n += s[i]
    return n