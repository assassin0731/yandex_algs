n = int(input())

maika = [int(x) for x in input().split()]

m = int(input())
shtani = [int(x) for x in input().split()]

minem = abs(maika[0] - shtani[0])

j = 0
i = 0
save_i = i
save_j = j

while i < n and j < m:
    now = abs(maika[i] - shtani[j])
    if minem > now:
        save_i = i
        save_j = j
        minem = now
    if maika[i] < shtani[j]:
        i += 1
    else:
        j += 1


print(maika[save_i], shtani[save_j])