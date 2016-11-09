#10_03 inputgen
from random import *
mini = -99
maxi = 100

radmax = 60
a = b = 0
n = 1000 # of circle
q = 1200 # of query
print n, q
for i in xrange(n):
    print randrange(mini, maxi), randrange(mini, maxi), randrange(1, radmax)
for i in xrange(q):
    while a == b:
        a, b = randrange(n), randrange(n)
    else:
        print a, b
        a = b = 0
