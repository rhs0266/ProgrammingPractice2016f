#10_03 inputgen
from random import *
mini = -100.0
maxi = 100.0

radmax = 60.0
a = b = 0
n = 1000 # of circle
q = 2000 # of query
print n, q
for i in xrange(n):
    print uniform(mini, maxi), uniform(mini, maxi), uniform(0.1, radmax)
for i in xrange(q):
    while a == b:
        a, b = randrange(n), randrange(n)
    else:
        print a, b
        a = b = 0
