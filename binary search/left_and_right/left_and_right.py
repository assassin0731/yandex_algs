def find_l(f, lister):
    l = 0
    r = len(lister)
    if lister[0] > f or lister[-1] < f:
        return 0
    while l < r:
        mid = (l + r) // 2
        if lister[mid] >= f:
            r = mid
        else:
            l = mid + 1
    if lister[l] != f:
        return 0
    return l + 1


def find_r(f, lister):
    l = 0
    r = len(lister)
    if lister[0] > f or lister[-1] < f:
        return 0
    while l < r:
        mid = (l + r) // 2
        if lister[mid] > f:
            r = mid
        else:
            l = mid + 1
    if lister[l - 1] != f:
        return 0
    return r


N = int(input())

lister = [int(x) for x in input().split()]

M = int(input())

find = [int(x) for x in input().split()]

for f in find:
    print(find_l(f, lister), find_r(f, lister))