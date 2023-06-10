str = input()
answer = ''
for i in str:
    if i.upper() != i:
        answer += i.upper()
    else:
        answer += i.lower()

print(answer)