def solution(num, total):
    start = 0
    if total % num == 0 & (total > num):
        start = (total // num) - num
    elif total < num:
        start -= total
    while True:
        check_list = list(range(start, (start+num)))
        if sum(check_list) == total:
            break
        start += 1
    return check_list