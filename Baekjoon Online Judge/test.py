n, m = map(int, input().split())
for _ in range(n):
    a, b = map(int, input().split())
    m += b if a == 1 else -b
print(m)