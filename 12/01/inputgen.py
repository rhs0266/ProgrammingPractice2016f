#12_01 inputgen
from random import randrange

n, m = 400, 499 #n x m array
mm = 9999

print n, m
for i in xrange(n):
    for j in xrange(m):
        print randrange(0, mm),
    print

print randrange(0, 4)
