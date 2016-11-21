#12_01 outputgen

n, m = map(int, raw_input().split())
arr = []
for i in xrange(n):
    arr.append(raw_input().split())

swi = input()

if swi == 0:
    for i in xrange(n):
        for j in xrange(m):
            print arr[i][j],
        print

if swi == 1:
    for i in xrange(m):
        for j in xrange(n):
            print arr[n - j - 1][i],
        print

if swi == 2:
    for i in xrange(n):
        for j in xrange(m):
            print arr[n - i - 1][m - j - 1],
        print

if swi == 3:
    for i in xrange(m):
        for j in xrange(n):
            print arr[j][m - i - 1],
        print
    
