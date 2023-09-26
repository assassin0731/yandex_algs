import sys
from collections import defaultdict

sys.setrecursionlimit(100000)

children = defaultdict(list)

N = int(input())
counter = {}


def counting(node, children, cnt=1):
    for ch in children[node]:
        counter[ch] = cnt
        counting(ch, children, cnt + 1)
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
counter[first_parent] = 0

for k, v in sorted(counter.items()):
    print(k, v)
