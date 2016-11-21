#12_04 outputgen
def gogo(direc, size):
    global posx, posy, count
    for i in xrange(size):
        arr[posy][posx] = count
        count += 1
        posy += go[direc][0]
        posx += go[direc][1]

size = input()
arr = [[0 for x in xrange(size)] for x in xrange(size)]
go = [(0, 1), (1, 0), (0, -1), (-1, 0)]
if size % 2 == 1:
    arr[size/2][size/2] = size * size
size -= 1
count, posx, posy = 1, 0, 0

while size >= 1:
    for i in xrange(4):
        gogo(i, size)
    posy += 1
    posx += 1
    size -= 2
    
for j in arr:
    for q in j:
        print q,
    print
