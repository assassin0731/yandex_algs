n, k = map(int, input().split())
s = input()
ss = dict.fromkeys(s, 0)
tl, tr, grl, grr = 0, 0, 0, 0
while tr < n:
    if ss[s[tr]] < k:
        if tr - tl > grr - grl:
            grr, grl = tr, tl
        ss[s[tr]] += 1
        tr += 1
    else:
        ss[s[tl]] -= 1
        tl += 1
print(grr - grl + 1, grl + 1)