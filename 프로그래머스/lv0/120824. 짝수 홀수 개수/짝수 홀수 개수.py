def solution(num_list):
    h, j = 0, 0
    for i in num_list:
        if i % 2 == 0:
            j += 1
        else: h += 1
    answer = [j, h]
    return answer