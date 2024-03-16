#2098: 외판원 순회
import sys
input = sys.stdin.readline
inf = int(1e9)
N = int(input())
W = [list(map(int,input().split())) for _ in range(N)]
dp = [[-1]*(1<<N) for _ in range(N)]

def dfs(x,mask):
    if mask == (1<<N)-1: return 0
    if dp[x][mask] > 0: return dp[x][mask]

    dp[x][mask] = inf
    for i in range(N):
        k = dfs(x+1,mask|1<<i)+W[x][mask]
        if dp[x][mask] > k:
            dp[x][mask] = k
    return dp[x][mask]

print(dfs(0,0))