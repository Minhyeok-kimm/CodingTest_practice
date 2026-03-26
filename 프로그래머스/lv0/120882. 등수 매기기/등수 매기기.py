def solution(score):
    score_mean = [sum(i)/len(i) for i in score]
    score_sort = sorted(score_mean, reverse=True)
    score_rank = []
    for i in score_mean:
        score_rank.append(score_sort.index(float(i))+1)
    return score_rank