def solution(a, d, included):
    target = [i for i in range(a, a+d*len(included), d)]
    return sum([j for j in target if included[target.index(j)] == True])