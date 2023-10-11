n, q = map(int, input().split())
lister = [int(x) for x in input().split()]

new_l = [0] * (len(lister) + 1)
for i in range(1, len(new_l)):
    new_l[i] = new_l[i - 1] + lister[i - 1]

pudge = []
for i in range(q):
    f, s = map(int, input().split())
    if f == s:
        pudge.append(lister[f - 1])
    else:
        pudge.append(new_l[s] - new_l[f] + lister[f - 1])

print(*pudge, sep='\n')