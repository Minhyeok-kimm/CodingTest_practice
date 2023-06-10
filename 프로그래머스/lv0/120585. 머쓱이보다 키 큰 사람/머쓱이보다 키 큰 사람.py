def solution(array, height):
    answer = 0
    n = len(array)
    for i in range(0, n):
        if array[i] > height:
            answer += 1
    return answer