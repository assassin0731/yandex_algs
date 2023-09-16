def bin_search(num, lister):
    l = 0
    r = len(lister) - 1
    while l <= r:
        mid = (l + r) // 2
        if lister[mid] == num:
            return 'YES'
        if lister[mid] > num:
            r = mid - 1
        else:
            l = mid + 1
    return 'NO'


N, K = map(int, input().split())

first = [int(x) for x in input().split()]
second = [int(x) for x in input().split()]

for s in second:
    print(bin_search(s, first))