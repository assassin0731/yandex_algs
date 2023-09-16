w, h, n = map(int, input().split())

L = max(w, h)

R = L * n

while L < R - 1:
    M = (L + R) // 2
    res = (M // w) * (M // h)
    if res < n:
        L = M
    else:
        R = M
        
print(R)