import sys

f = sys.stdin.read()

f = f.split('\n')

def addzeros(num):
    x, y = num.split('.')
    if len(y) == 1:
        return num + '0'
    return num

for line in f:
    x, y = list(map(float, line.split(' ')))
    if x != 0:
        print(addzeros(str(round(x*10**y, 2))))
