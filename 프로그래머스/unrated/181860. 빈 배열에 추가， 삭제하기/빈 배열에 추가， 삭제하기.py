def solution(arr, flag):
    answer = []
    for i in range(len(arr)):
        if flag[i]:
            for a in range(arr[i] * 2):
                answer.append(arr[i])
        else:
            for k in range(arr[i]):
                answer.pop()
    return answer