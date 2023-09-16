def bin_search(num, lister):
    l = 0
    r = len(lister) - 1
    while l < r - 1:
        mid = (l + r) // 2
        if lister[mid] == num:
            return num
        if lister[mid] > num:
            r = mid
        else:
            l = mid
    if num - lister[l] <= lister[r] - num:
        return lister[l]
    else:
        return lister[r]


N, K = map(int, input().split())

first = [int(x) for x in input().split()]
second = [int(x) for x in input().split()]

for s in second:
    print(bin_search(s, first))