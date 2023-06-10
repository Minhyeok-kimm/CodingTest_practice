def solution(numbers):
    numbers.sort()
    return numbers.pop() * max(numbers)