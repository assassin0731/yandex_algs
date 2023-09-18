n, a, b, w, h = map(int, input().split())

L = 0

R = min(w, h)

while L < R - 1:
    d = (L + R) // 2
    res = max((h // (a + 2 * d)) * (w // (b + 2 * d)), (w // (a + 2 * d)) * (h // (b + 2 * d)))
    if res >= n:
        L = d
    else:
        R = d

print(L)