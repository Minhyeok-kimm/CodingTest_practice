def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        return eval('*'.join([str(i) for i in num_list]))