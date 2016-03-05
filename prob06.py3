import sys

f = sys.stdin.read()

f = f.split('\n')

times = int(f.pop(0))

def removezeros(num):
    x, y = str(num).split('.')
    if y == '0':
        return x
    return num

for i in range(times):
    a, x1, x2, y1, y2 = list(map(int, f[i].split()))

    slope = (y2-y1)/(x2-x1)

    b = y1 - slope * x1

    print(removezeros((a * slope + b)/8.0))