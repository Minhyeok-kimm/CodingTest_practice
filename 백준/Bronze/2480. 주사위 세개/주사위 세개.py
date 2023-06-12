a, b, c = map(int, input().split())
dictl = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
dictl[a] += 1
dictl[b] += 1
dictl[c] += 1
new_dict = {v:k for k, v in dictl.items()}

if len(set([a, b, c])) == 1:
    print(10000 + (new_dict[3] * 1000))
elif len(set([a, b, c])) == 2:
    print(1000 + (new_dict[2] * 100))
else:
    print(max(a, b, c) * 100)