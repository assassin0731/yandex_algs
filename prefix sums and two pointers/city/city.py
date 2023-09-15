n, r = map(int, input().split())
lister = [int(x) for x in input().split()]

counter = 0

i = 0
j = 1

for i in range(n):
    while j < n - 1 and lister[j] - lister[i] <= r:
        j += 1
    if lister[j] - lister[i] > r:
        counter += n - j
    else:
        break


print(counter)