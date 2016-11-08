#10_03 outputgen
n, q = map(int, raw_input().split())
a = []
b = []
c = []

for i in xrange(n):
    t = map(int, raw_input().split())
    a.append(t[0])
    b.append(t[1])
    c.append(t[2])

for i in xrange(q):
    z, x = map(int, raw_input().split())
    dist = (a[z] - a[x]) ** 2 + (b[z] - b[x]) ** 2
    if dist < (c[z] + c[x]) ** 2 and dist > (c[z] - c[x]) ** 2:
        print "yes"
    else:
        print "no"
