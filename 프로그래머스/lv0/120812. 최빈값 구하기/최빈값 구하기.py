def solution(array):
    dic = dict()
    for i in array:
        try:
            dic[i] += 1
        except:
            dic[i] = 1
    lst = list(dic.values())
    counts = max(lst)
    if lst.count(counts) != 1:
        return -1
    else:
        new_dict = {v:k for k, v in dic.items()}
        return new_dict[counts]