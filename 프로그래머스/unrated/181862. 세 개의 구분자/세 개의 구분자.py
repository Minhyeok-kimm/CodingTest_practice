def solution(myStr):
    lst = []
    st = myStr.replace('a', '!').replace('b', '!').replace('c', '!')
    s = ''
    for i in range(len(st)):
        if st[i] != '!':
            s += myStr[i]
        elif st[i] == '!':
            if s != '':
                lst.append(s)
                s = ''
    if s != '':
        lst.append(s)
    return lst if lst else ["EMPTY"]