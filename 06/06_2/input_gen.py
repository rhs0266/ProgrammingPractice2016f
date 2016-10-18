#generator for 06_2

from random import * 

N = 1000
print N
#p = [x for x in xrange(N)]
p = []
for i in xrange(N):
    p.append(randrange(1, 1000000))
    
shuffle(p)
for i in p:
    print i,
