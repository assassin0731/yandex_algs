def find_l(new, lister1):
    l = 0
    r = len(lister1)
    while l < r:
        mid = (l + r) // 2
        if lister1[mid] >= new:
            r = mid
        else:
            l = mid + 1
    return l

def find_r(new, lister1):
    l = 0
    r = len(lister1)
    while l < r:
        mid = (l + r) // 2
        if lister1[mid] > new:
            r = mid
        else:
            l = mid + 1
    return r

N = int(input())

lister = [int(x) for x in input().split()]
lister.sort()


K = int(input())

newer = []

for i in range(K):
    l, r = map(int, input().split())
    newer.append(find_r(r, lister) - find_l(l, lister))

print(*newer)