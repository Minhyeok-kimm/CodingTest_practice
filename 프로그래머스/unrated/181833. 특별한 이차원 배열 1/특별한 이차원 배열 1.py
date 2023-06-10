def solution(n):
    answer = []
    for i in range(n):
        answer.append([])
        for j in range(n):
            answer[i].append(1 if i == j else 0)
    return answer