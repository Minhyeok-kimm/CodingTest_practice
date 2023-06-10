def solution(rank, attendance):
    arr = []
    for i in range(1, len(rank)+1):
        if attendance[rank.index(i)]:
            arr.append(rank.index(i))
    return 10000 * arr[0] + 100 * arr[1] + arr[2]