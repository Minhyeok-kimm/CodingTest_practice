def solution(num_list):
    target1 = sum(num_list) ** 2
    target2 = eval('*'.join([str(i) for i in num_list]))
    return 1 if target2 < target1 else 0