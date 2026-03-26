def solution(my_string):
    string_list = list(my_string.split(" "))
    answer = int(string_list[0])
    for i in range(1, len(string_list), 2):
        if string_list[i] == "+":
            answer += int(string_list[i+1])
        else:
            answer -= int(string_list[i+1])
    return answer