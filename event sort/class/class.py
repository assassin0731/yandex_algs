N = int(input())

lister = []
opened = 0

for i in range(N):
    open_h, open_m, close_h, close_m = map(int, (input().split()))
    if open_h * 60 + open_m > close_h * 60 + close_m:
        lister.append((open_h * 60 + open_m, 1))
        lister.append((24 * 60, 0))
        lister.append((0, 1))
        lister.append((close_h * 60 + close_m, 0))
        continue
    if open_h == close_h and open_m == close_m:
        lister.append((0, 1))
        lister.append((24 * 60, 0))
    lister.append((open_h * 60 + open_m, 1))
    lister.append((close_h * 60 + close_m, 0))


lister.sort()

counter = 0

for i in range(len(lister)):
    if opened == N:
        counter += lister[i][0] - lister[i - 1][0]
    if lister[i][1] == 1:
        opened += 1
    if lister[i][1] == 0:
        opened -= 1


print(counter)
