def solution(num_list):
    answer = []
    n = len(num_list)
    for i in range(n, 0, -1):
        answer.append(num_list[i-1])
    
    return answer