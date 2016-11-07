#inputgen 10-1
from random import *
n = 80000 # number
q = 80000 #query
fromchoice = 50000 # choice
maxi = 2 ** 31 - 1 # max
mini = -1 * 2 ** 31 # min
arr = []

print n, q
while len(set(arr)) != n:
    arr.append(randrange(mini, maxi))
arr = sorted(arr)
#for i in xrange(n):
    #arr.append(i - 2 ** 30)
for a in arr:
    print a,
print
for i in xrange(fromchoice):
    print choice(arr),
for i in xrange(q - fromchoice):
    print randrange(mini, maxi),
print
