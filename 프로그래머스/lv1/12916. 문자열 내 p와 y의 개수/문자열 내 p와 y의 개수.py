def solution(s):
    # 대소문자 구별하지 않기 때문에 한 가지로 통일
    data = s.lower()
    # p와 y 개수가 같거나 없는 경우 True / 아니면 False 반환
    if data.count('p') == data.count('y') or data.count('p') == data.count('y') == 0:
        return True
    else:
        return False