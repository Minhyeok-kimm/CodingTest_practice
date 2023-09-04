def solution(n):
    import math
    # 제곱근 처리
    m = math.sqrt(n)
    # int를 적용한 값과 같을 시 양의 정수 x의 제곱으로 판단
    if int(m) == m:
        return (m+1) * (m+1)
    else:
        return -1