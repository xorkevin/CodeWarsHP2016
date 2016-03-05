import sys

f = sys.stdin.read()

f = f.split('\n')

f.pop()

for line in f:
    if line != "=========":
        chars = list(line)
        box = []
        for i in range(3):
            temp = []
            for j in range(3):
                temp.append(chars.pop(0))
            box.append(temp)
        winner = "Z"
        for r in range (3):
            curr = box[r][0]
            if(curr == box[r][1] and curr == box[r][2]):
                winner = curr
        for c in range(3):
            curr = box[0][c]
            if(curr == box[1][c] and curr == box[2][c]):
                winner = curr

        curr = box[0][0]
        if(curr == box[1][1] and curr == box[2][2]):
                winner = curr
        curr = box[0][2]
        if(curr == box[1][1] and curr == box[2][0]):
                winner = curr
        if(winner == "Z"):
            print ("There was a tie.")
        else:
            print("Player " + winner + " won.")
        for line in box:
            print(''.join(line))
        print('')
