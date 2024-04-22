#23829: 인문예술탐사주간
import sys
input = sys.stdin.readline
N,Q = map(int,input().split())
P = [0]+sorted(list(map(int,input().split())))

def binsearch(t):
    s,e = 0,N-1
    while s < e:
        m = (s+e)//2
        if P[m] > t:
            e = m-1
        else:
            s = m
        if e-s == 1:
            if P[e] > t:
                return s
            else:
                return e
    return s

prepix = [0]*(N+1)
prepix[0] = P[0]
for i in range(1,N+1):
    prepix[i] = prepix[i-1]+P[i]
for _ in range(Q):
    X = int(input())
    t = binsearch(X)
    a = t*X-prepix[t]
    b = abs(prepix[-1]-prepix[t]-(N-t)*X)
    print(a+b)