def solution(arr):
    answer = arr.copy()
    x = 0
    while True:
        vs = answer.copy()
        for i in range(len(answer)):
            if (answer[i] >= 50) & (answer[i]%2 == 0):
                answer[i] = answer[i]/2
            elif (answer[i] < 50) & (answer[i]%2 == 1):
                answer[i] = answer[i]*2+1
        if answer == vs:
            break
        else:
            x += 1
    return x