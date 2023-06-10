def solution(my_string):
    st = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    ans = [0 for i in range(len(st))]
    for i in range(len(st)):
        for j in range(len(my_string)):
            if my_string[j] == st[i]:
                ans[i] = ans[i] + 1
    return ans