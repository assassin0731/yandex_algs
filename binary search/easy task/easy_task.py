N, x, y = map(int, input().split())

l = min(x, y)
start = l
r = max(x, y) * (N - 1)
N -= 1

while l < r:
    m = (l + r) // 2
    if m // x + m // y < N:
        l = m + 1
    else:
        r = m


print(r + start)