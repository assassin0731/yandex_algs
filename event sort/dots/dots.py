n, m = map(int, input().split())

lister = []

for i in range(n):
    first, last = map(int, input().split())
    lister.append((min(first, last), '('))
    lister.append((max(first, last), ')'))


dots = [int(x) for x in input().split()]


for d in dots:
    lister.append((d, "(("))


lister.sort()

k = 0
dicter = dict()

for li in lister:
    if li[1] == '(':
        k += 1
    elif li[1] == ')':
        k -= 1
    else:
        dicter[li[0]] = k


for i in dots:
    print(dicter[i], end=" ")
