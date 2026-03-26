def solution(numbers):
    num_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i, j in enumerate(num_list):
        if j in numbers:
            numbers = numbers.replace(j, str(i))
    return int(numbers)