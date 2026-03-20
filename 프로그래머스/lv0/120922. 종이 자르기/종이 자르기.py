def solution(M, N):
    if M == 1 or N == 1:
        return (M - 1) + (N - 1)
    else:
        return (min(M, N) - 1) + (max(M, N) - 1) * min(M, N)