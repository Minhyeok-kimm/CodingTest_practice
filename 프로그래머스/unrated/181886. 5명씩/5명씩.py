def solution(names):
    if len(names) <= 5:
        return [names[0]]
    else:
        return names[0::5]