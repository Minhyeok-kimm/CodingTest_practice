def solution(arr, k):
    answer = []
    i = 0
    while len(answer) != k:
        if i >= len(arr):
            answer.append(-1)
        elif answer.count(arr[i]) == 0:
            answer.append(arr[i])
        i += 1
    return answer