def solution(arr):
    answer = []
    i = 0
    while i < len(arr):
        if len(answer) == 0:
            answer.append(arr[i])
            i += 1
        elif answer[-1] == arr[i]:
            answer.pop()
            i += 1
        else:
            answer.append(arr[i])
            i += 1
    return answer if len(answer) else [-1]