import sys

def hasDouble(word):
    letters = list(set(list(word)))
    if len(''.join(letters)) < len(word):
        return True
    return False


f = sys.stdin.read()

f = f.split('\n')

skip = False

for line in f:
    if skip:
        if hasDouble(line):
            print('likes ' + line)
        else:
            print('hates ' + line)
    else:
        skip = True
