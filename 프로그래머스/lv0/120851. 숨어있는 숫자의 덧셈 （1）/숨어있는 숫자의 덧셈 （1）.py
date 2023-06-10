def solution(my_string):
    l = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return sum([int(i) for i in my_string if i not in l])