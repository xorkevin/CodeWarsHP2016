import sys

f = sys.stdin.read()

f = f.split('\n')

for line in f:
    aku = list(filter(lambda tup: tup != '', line.split(' ')))
    a, b, c = aku