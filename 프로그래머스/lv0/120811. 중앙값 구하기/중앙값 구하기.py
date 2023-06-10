def solution(array):
    array.sort()
    a = len(array)
    l = a // 2
    answer = array[l]
    return answer