def solution(participant, completion):
    part = {}
    for i in participant:
        if i not in part.keys():
            part[i] = 1
        else:
            part[i] += 1
    for i in completion:
        part[i] -= 1
    for i in participant:
        if part[i] != 0:
            return i