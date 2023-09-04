def solution(n):
    # 리스트로 숫자 하나씩 반환
    lst = [i for i in str(n)]
    # 내림차순 정렬
    lst.sort(reverse=True)
    # 리스트를 다시 합친 후 int로 반환
    answer = "".join(lst)
    return int(answer)