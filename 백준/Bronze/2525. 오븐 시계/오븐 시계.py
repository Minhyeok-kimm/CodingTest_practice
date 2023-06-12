A, B = map(int, input().split())
C = int(input())
B = B + C
if B > 59:
    if A + B//60 > 23:
        print(A + B//60 - 24, B - (60 * (B//60)))
    else:
        print(A + B//60, B - (60 * (B//60)))
else:
    print(A, B)