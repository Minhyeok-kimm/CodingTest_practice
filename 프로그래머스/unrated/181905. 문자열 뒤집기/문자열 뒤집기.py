def solution(my_string, s, e):
    lst = [my_string[i] for i in range(len(my_string))]
    lst[s:e+1] = reversed(lst[s:e+1])
    return ''.join(lst)