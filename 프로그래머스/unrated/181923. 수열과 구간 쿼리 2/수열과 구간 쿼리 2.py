def solution(arr, queries):
    answer = []
    for a, b, c in queries:
        l = []
        for idx in range(len(arr)):
            if (a <= idx <= b) and (arr[idx] > c):
                l.append(arr[idx])
        answer.append(min(l)) if len(l) != 0 else answer.append(-1)
    return answer