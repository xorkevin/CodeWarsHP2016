import sys

def func(letterList, nextWord):
    tempList = []

    kevin = list(nextWord)
    for i in range(len(letterList)):
        letter = letterList[i]
        try:
            kevin.remove(letter)
            tempList.append(letter)
        except ValueError:
            pass
    return tempList

f = sys.stdin.read()

f = f.split('\n')

times = int(f.pop(0))

for i in range(times):
    aku = list(filter(lambda tup: tup != '', f[i].split(' ')))
    a, b, c = aku

    letters = []

    letterList = list(a)

    letterList = func(letterList, b)

    letterList = func(letterList, c)

    print(''.join(sorted(letterList)))