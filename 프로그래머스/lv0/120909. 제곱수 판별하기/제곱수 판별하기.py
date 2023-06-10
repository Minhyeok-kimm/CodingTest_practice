def solution(n):
    answer = 0
    for i in range(n):
        if i ** 2 == n:
            answer = 1
    
    return 2 if answer == 0 else answer