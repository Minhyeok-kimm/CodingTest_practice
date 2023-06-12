H, M = map(int, input().split())
M -= 45
if M < 0:
    if H-1 < 0:
        print(H + 23, M + 60)
    else:
        print(H - 1, M + 60)
else:
    print(H, M)