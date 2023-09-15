def summ_num(numbers):
    summer = [0] * (len(numbers) + 1)
    for i in range(1, len(summer)):
        summer[i] = summer[i - 1] + numbers[i - 1]
    return summer

N, K = map(int, input().split())
lister = [int(x) for x in input().split()]
summer = summ_num(lister)

i = 0
j = 1
counter = 0

while i != N + 1 and j != N + 1:
    if summer[j] - summer[i] == K:
        counter += 1
        i += 1
        j += 1
    elif summer[j] - summer[i] < K:
        j += 1
    elif summer[j] - summer[i] > K:
        i += 1

print(counter)
