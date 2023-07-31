def solution(array, n):
    # 전체 배열에 넣어 리스트 생성 후 정렬
    array.append(n)
    array.sort()
    # n의 인덱스 값 추출
    idx = array.index(n)
    # n이 마지막에 위치할 경우
    if idx == len(array)-1:
        # n 직전 위치의 값 반환
        return array[idx-1]
    # n 직전 위치와의 차이가 더 큰 경우
    elif (n - array[idx-1]) > (array[idx+1] - n):
        # n 이후 위치의 값 반환
        return array[idx+1]
    # n 이후 위치와의 차이가 더 크거나 차이가 같은 경우
    elif (n - array[idx-1]) < (array[idx+1] - n) or (n - array[idx-1]) == (array[idx+1] - n):
        # n 이전 위치의 값 반환
        return array[idx-1]