def solution(arr):
    answer = []
    for i in arr:
        x = 0
        while x != i:
            answer.append(i)
            x += 1
    return answer