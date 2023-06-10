def solution(num_list):
    odd = ''.join([str(i) for i in num_list if i%2 == 1])
    even = ''.join([str(j) for j in num_list if j%2 == 0])
    return int(odd) + int(even)