N = int(input())

lister = [list(map(int, input().split())) for i in range(N)]

up = [0] * N
down = [0] * N

for i in range(1, N):
    val = lister[i][1] - lister[i - 1][1]
    if val > 0:
        up[i] = up[i - 1] + val
        down[i] = down[i - 1]
    else:
        down[i] = down[i - 1] - val
        up[i] = up[i - 1]

M = int(input())

lister = [list(map(int, input().split())) for i in range(M)]


for li in lister:
    if li[0] < li[1]:
        print(up[li[1] - 1] - up[li[0] - 1])
    else:
        print(down[li[0] - 1] - down[li[1] - 1])