def solution(arr):
    n = 0
    while len(arr) != 2**n:
        if len(arr) > 2**n:
            n += 1
        elif len(arr) < 2**n:
            arr.append(0)
    return arr