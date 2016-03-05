import sys, math

class Star:
    def __init__(self, name, x, y, z):
        self.name = name
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return self.name == other.name



class Node:
    def __init__(self, star, parent, g, f):
        self.star = star
        self.parent = parent
        self.g = g
        self.f = f


def distance(star1, star2):
    return math.sqrt( (star2.x - star1.x)**2 +(star2.y - star1.y)**2 + (star2.z - star1.z)**2 )

f = sys.stdin.read()

f = f.split('\n')

times = int(f.pop(0))

notvisited = []
starBank = []
queue = []

for i in range(times):
    name, _, _, x, y, z = f.pop(0).split()
    starBank.append(Star(name, x, y, z))

times = int(f.pop(0))
for i in range(times):
    notvisited = starBank
    start, goal, max = f.pop(0).split()

    queue.append(Node(notvisited.remove(start), -1, 0, 0))


    queue.append()

    currentNode = Node(start, -1, 0, 0, distance(start, goal))

    currentNode = queue.pop(0)
    starBank.remove(currentNode.star)

    for destStar in notvisited:
        if(distance(currentNode.star, destStar) <= max):
            queue.append(Node(destStar, currentNode.star,
                              currentNode.g + distance(currentNode.star, destStar), 0))


