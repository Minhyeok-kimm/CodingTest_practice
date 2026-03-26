def solution(A, B):
    A_list = [A[i] for i in range(len(A))]
    answer = 0
    AB_diff = True
    for i in range(len(A_list)):
        if ''.join(A_list) == B:
            AB_diff = False
        else:
            answer += 1
            last_str = A_list.pop()
            A_list.insert(0, last_str)
        if AB_diff:
            continue
        else:
            return answer
    return -1