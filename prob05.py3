import sys

f = sys.stdin.read()

f = f.split('\n')

f.pop(0)
f.pop()

for line in f:
    x, y = line.split(' ')
    x = int(x)
    y = list(enumerate(y))

    y = list(filter(lambda tup: tup[0]%x != 0, y))

    k = ''
    for tup in y:
        k += tup[1]
    print('' + str(k) + ' ' + str(len(k)))