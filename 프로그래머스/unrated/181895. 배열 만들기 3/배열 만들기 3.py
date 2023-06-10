def solution(arr, intervals):
    answer = []
    for i, j in intervals:
        answer = answer + arr[i:j+1]
    return answer