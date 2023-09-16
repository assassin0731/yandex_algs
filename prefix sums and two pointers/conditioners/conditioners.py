n = int(input())

lister = [int(x) for x in input().split()]

m = int(input())

dicter = {}

for i in range(m):
    key, val = map(int, input().split())
    if key not in dicter or dicter[key] > val:
        dicter[key] = val


original_dict = dicter
filtered = filtered_dict = {key: value for key, value in original_dict.items()
                            if all(value <= original_dict[next_key] for next_key in original_dict if next_key > key)}

dicter = filtered
counter = 0
j = 0
s_dicter = sorted(dicter)
lenger = len(s_dicter)

for val in sorted(lister):
    while val > s_dicter[j]:
        j += 1
    counter += dicter[s_dicter[j]]

print(counter)