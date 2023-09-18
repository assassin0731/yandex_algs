N, K = map(int, input().split())

lister = [int(input()) for _ in range(N)]

l = 1
r = 1000000000

while l < r:
    mid = (l + r) // 2
    counter = 0
    for li in lister:
        counter += li // mid
    if counter >= K:
        l = mid + 1
    else:
        r = mid


print(l - 1)