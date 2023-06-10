import math

def solution(price):
    answer = price
    if price < 100000:
        answer = price
    elif price < 300000:
        answer = math.floor(price * 0.95)
    elif price < 500000:
        answer = math.floor(price * 0.9)
    else:
        answer = math.floor(price * 0.8)
    return answer