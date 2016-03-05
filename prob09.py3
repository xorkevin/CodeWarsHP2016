import sys

f = sys.stdin.read()

f = f.split('\n')

f.pop()
f.pop()

for line in f:
    a, b, c = line.split(' ')
    l = int(a)
    w = int(b)
    h = int(c)

    painted = 2*l*w + 2*w*(h-2) + 2*((l-2) * (h-2))

    aku = l*w*h - painted

    k = ''

    if aku == painted:
        k = 'PERFECT.'
    elif aku < painted:
        k = 'MORE than Perfect.'
    else:
        k = 'LESS than Perfect.'

    print('A {}x{}x{} block is {}'.format(l, w, h, k))
