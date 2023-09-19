N, M = map(int, input().split())

lister = []

for i in range(M):
    first, last = map(int, input().split())
    lister.append((first, last))

lister.sort()
counter = 0

for l in lister:
    if counter == 0:
        minem = l[0]
        maxem = l[1]
        counter += maxem - minem + 1
    else:
        if l[1] > maxem:
            minem = max(maxem, l[0])
            if minem == maxem:
                minem += 1
            maxem = l[1]
            counter += maxem - minem + 1

print(N - counter)
