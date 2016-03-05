import sys

f = sys.stdin.read()

f = f.split('\n')
f.pop()

f = list(map(int, f))
f.pop()

for line in f:
    k = int(10000/line)
    print('' + str(line) + ' gallons per week will last ' + str(k) + ' weeks')