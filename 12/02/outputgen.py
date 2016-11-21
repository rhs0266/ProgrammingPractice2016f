#12_02 outputgen
n, m = map(int, raw_input().split())
narr = map(int, raw_input().split())
marr = map(int, raw_input().split())
aarr = []
for i in xrange(n + m + 1):
    aarr.append(0)

for i in xrange(n + 1):
    for j in xrange(m + 1):
        aarr[i + j] += narr[i] * marr[j]

for i in xrange(n + m + 1):
    print aarr[i],
print
    
