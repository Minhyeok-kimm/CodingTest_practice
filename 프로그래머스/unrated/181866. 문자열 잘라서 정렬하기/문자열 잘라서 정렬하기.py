def solution(myString):
    lst = myString.split('x')
    if lst.count('') > 0:
        for i in range(lst.count('')):
            lst.remove('')
    return sorted(lst)