from sys import stdin
from collections import defaultdict


children = defaultdict(list)

N = int(input())


first_parent = None

for _ in range(N - 1):
    ch, parent = input().split()
    children[ch] = parent

for line in stdin:
    f, s = line.split()
    first = set()
    second = set()
    first.add(f)
    second.add(s)
    while len(first & second) == 0:
        new_f = children.get(f, '0')
        new_s = children.get(s, '0')
        f = new_f
        s = new_s
        first.add(new_f)
        second.add(new_s)
    print(''.join(set(first) & set(second)))





