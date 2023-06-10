def solution(arr):
    answer = []
    for i in range(len(arr)):
        if arr[i] == 2:
            answer.append(i)
    if len(answer) > 1:
        return arr[min(answer):max(answer)+1]
    elif len(answer) == 1:
        return [2]
    else:
        return [-1]