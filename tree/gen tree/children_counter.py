import sys
from collections import defaultdict
from itertools import chain

sys.setrecursionlimit(100000)

children = defaultdict(list)

N = int(input())


def counting(node, children):
    cnt = 0
    for ch in children[node]:
        cnt += 1 + counting(ch, children)
    children[node].append(cnt)
    return cnt


first_parent = None

for _ in range(N - 1):
    ch, parent = input().split()
    children[parent].append(ch)

seter = set(sum(children.values(), []))

for key in children.keys():
    if key not in seter:
        first_parent = key
        break

counting(first_parent, children)

for k, v in sorted(children.items()):
    print(k, v[-1])
