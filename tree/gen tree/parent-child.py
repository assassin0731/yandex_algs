from sys import stdin
from collections import defaultdict


children = defaultdict(list)

N = int(input())


first_parent = None

for _ in range(N - 1):
    ch, parent = input().split()
    children[parent].append(ch)

for line in stdin:
    check = False
    f, s = line.split()
    stack = [children[f]]
    while stack:
        v = stack.pop()
        if s in v:
            check = True
            print(1)
            break
        else:
            for vi in v:
                stack.append(children[vi])
    stack = [children[s]]
    while stack:
        v = stack.pop()
        if f in v:
            print(2)
            check = True
            break
        else:
            for vi in v:
                stack.append(children[vi])
    if not check:
        print(0)




