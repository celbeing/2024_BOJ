# 1955: 수식 표현
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    dp = [i for i in range(n + 1)]
    k = 1
    fac = 1
    f = dict()
    while fac <= n:
        f[fac] = k
        k += 1
        fac *= k
    for i in range(2, n + 1):
        for j in range(1, i):
            dp[i] = min(dp[i], dp[i - j] + dp[j])
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[i // j] + dp[j])
        if i in f:
            if dp[i] > dp[f[i]]:
                dp[i] = dp[f[i]]
    print(dp[n])
solution()