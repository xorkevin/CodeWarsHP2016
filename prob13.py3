import sys, math

f = sys.stdin.read()

f = f.split('\n')

f.pop(0)
f.pop()

for line in f:
    aku = list(filter(lambda tup: tup != '', line.split(' ')))
    a, b, c, d, e, _, _, ly = aku

    b = float(b)
    c = float(c)
    d = float(d)
    e = float(e)
    ly = float(ly)

    ra = 0
    dec = 0

    if b >= 0:
        ra = b*15 + c*0.25
    else:
        ra = b*15 - c*0.25

    if d >= 0:
        dec = d+e/60.0
    else:
        dec = d-e/60.0

    theta = (90-dec) * 3.1415926535 / 180.0
    trident = ra * 3.14159265 / 180.0

    x = ly * math.sin(theta)*math.cos(trident)
    y = ly * math.sin(theta)*math.sin(trident)
    z = ly * math.cos(theta)

    x = round(float(x), 2)
    y = round(float(y), 2)
    z = round(float(z), 2)

    print('{} x={}, y={}, z={}'.format(a, x, y ,z))