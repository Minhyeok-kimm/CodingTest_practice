def solution(myString):
    s = 'abcdefghijk'
    lst = [myString[i] for i in range(len(myString))]
    for j in range(len(lst)):
        if lst[j] in s:
            lst[j] = 'l'
    return ''.join(lst)