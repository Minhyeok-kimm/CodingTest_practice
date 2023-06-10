def solution(arr, idx):
    answer = -1
    for i in range(idx, len(arr)):
        if arr[i] == 0:
            pass
        else:
            answer = i
            break
    return answer