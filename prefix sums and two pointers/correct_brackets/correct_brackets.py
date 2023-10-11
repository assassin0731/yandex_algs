streng = input()

counter = 0
printed = False
for s in streng:
    if s == '(':
        counter += 1
    else:
        counter -= 1
    if counter < 0:
        print('NO')
        printed = True
        break

if not printed and counter > 0:
    print('NO')
elif not printed:
    print('YES')