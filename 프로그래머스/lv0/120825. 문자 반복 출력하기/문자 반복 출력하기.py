def solution(my_string, n):
    answer = str('')
    for i in range(len(my_string)):
        for j in range(n):
            answer = answer + my_string[i]
    return answer