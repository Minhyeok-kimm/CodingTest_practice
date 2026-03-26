def solution(quiz):
    answer = []
    for i in quiz:
        check = i.split(" ")
        if "+" in check:
            if int(check[0]) + int(check[2]) == int(check[-1]):
                answer.append("O")
            else:
                answer.append("X")
        else:
            if int(check[0]) - int(check[2]) == int(check[-1]):
                answer.append("O")
            else:
                answer.append("X")
    return answer