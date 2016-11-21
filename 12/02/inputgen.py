#12_02 inputgen
import random
n, m = 999, 999
mm = 500
print n, m

print random.randrange(1, mm),
for i in xrange(n):
    print random.randrange(mm),
print
print random.randrange(1, mm),
for j in xrange(m):
    print random.randrange(mm),
print
