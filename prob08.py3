import sys

def increaseToLength(lets, length, end = False):
    a = lets
    while len(a) < length:
        if end:
            a += ' '
        else:
            a = ' ' + a
    return a


f = sys.stdin.read()

f = f.split('\n')

times = int(f.pop(0))

for i in range(times):
    letArray = list(f[i])

    lenArray = len(letArray)

    # rows = lenArray
    #
    # cols = rows*2 - 1
    #
    # box = []
    #
    # for j in range(rows):
    #     tempArray = []
    #     for k in range(cols):
    #         tempArray.append(' ')
    #     box.append(tempArray)
    #
    # for j in range(lenArray):
    #     m = 0
    #     c = letArray[j]
    #
    #     for n in range(lenArray):
    #         box[m+i][lenArray-n] = c
    #         m += 1

    kevin = []
    kevin2 = []

    # NEW
    for j in range(lenArray):
        temp = []
        for k in range(j+1):
            temp.append(letArray[k])
        kevin.append(increaseToLength(''.join(temp), lenArray))
    for j in range(1, lenArray):
        temp = []
        for k in range(j):
            temp.append(letArray[lenArray-k-1])
        kevin2.append(increaseToLength(''.join(list(reversed(temp))), lenArray, True))

    kevin2 = list(reversed(kevin2))

    for line in kevin:
        print(line)
    for line in kevin2:
        print(line)
