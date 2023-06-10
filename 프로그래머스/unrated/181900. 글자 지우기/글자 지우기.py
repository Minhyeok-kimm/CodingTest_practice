def solution(my_string, indices):
    lst = [my_string[i] for i in range(len(my_string))]
    indices.sort(reverse=True)
    for i in indices:
        del lst[i]
    return ''.join(lst)