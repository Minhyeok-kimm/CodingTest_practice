def solution(my_strings, parts):
    answer = ''
    for i in my_strings:
        x, y = parts[my_strings.index(i)]
        answer += i[x:y+1]
    return answer