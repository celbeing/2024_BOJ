#1725: 히스토그램
import sys
input = sys.stdin.readline

N = int(input())
s = [0]
arr = [0]
big = 0
for n in range(1, N+2):
    if n == N+1:
        h = 0
    else:
        h = int(input())
    arr.append(h)
    if arr[s[-1]] <= h:
        s.append(n)
    else:
        while arr[s[-1]] > h:
            now = arr[s.pop()] * (n-s[-1]-1)
            if now > big:
                big = now
        now = arr[s[-1]]
        s.append(n)
print(big)