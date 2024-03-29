#20040: 사이클 게임
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n,m = map(int,input().split())
union = [i for i in range(n)]

def find(k):
    while union[k] != k:
        k = union[k]
    return k

result = 0
for i in range(1,m+1):
    a,b = map(int,input().split())
    A = find(a)
    B = find(b)
    if A == B:
        result = i
        break
    union[B] = A
print(result)