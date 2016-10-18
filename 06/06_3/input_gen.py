#generator for 06_3

from random import * 

N = 10000
M = 10000
MAX = 1000000
print N, M
#p = [x for x in xrange(N)]
na = []
ma = []
for i in xrange(N):
    na.append(randrange(1, MAX))
for i in xrange(M):
    ma.append(randrange(1, MAX))
    
for i in sorted(na):
    print i,
print 
for i in sorted(ma):
    print i,
